/* Controllers */
// tournaments (main page) controller
app.controller('PageTournamentController', ['$scope', 'tournamentById', '$stateParams', '$q', '$interval', 'attendants', 'attendantsByTournamentId',
    'djangoAuth', 'tournamentAttendantsById', 'tournamentDataById',
    function ($scope, tournamentById, $stateParams, $q, $interval, attendants, attendantsByTournamentId, djangoAuth, tournamentAttendantsById, tournamentDataById) {

        var dateToStart = null;
        $scope.isAlreadyAttendant = false;
        $scope.isNotStarted = false;
        $scope.isCanceled = false;

        function formatDate(d) {
            var day = d.getDate();
            var monthIndex = d.getMonth() + 1;

            if (day < 10) day = "0" + day;
            if (monthIndex < 10) monthIndex = "0" + monthIndex;

            return day + "." + monthIndex;
        }

        function formatTime(d) {
            var hours = d.getHours();
            var minutes = d.getMinutes();

            if (hours < 10) hours = "0" + hours;
            if (minutes < 10) minutes = "0" + minutes;

            return hours + ":" + minutes;
        }

        //d1 - datetostart d2 - now
        function calcDiff(d1, d2) {
            if (d1 > d2) {
                var diff = d2 - d1, sign = diff < 0 ? -1 : 1, milliseconds, seconds, minutes, hours, days;
                diff /= sign; // or diff=Math.abs(diff);
                diff = (diff - (milliseconds = diff % 1000)) / 1000;
                diff = (diff - (seconds = diff % 60)) / 60;
                diff = (diff - (minutes = diff % 60)) / 60;
                days = (diff - (hours = diff % 24)) / 24;
                return days + " дней, " + hours + " часов, " + minutes + " минут, " + seconds + " секунд."
            } else {
                return "турнир уже начался.";
            }
        }

        function calcPositionOnGraph(created, start, value) {
            var x1 = 25;//created_at - x coordinate
            var x2 = 499;//date(start) - x coordinate

            var total = start - created;
            var progress = value - created;
            var percent = progress / total;
            return (x2 - x1) * percent + x1;
        }


        function calcDatesForGraph(data) {
            //start date
            dateToStart = new Date(data.date);
            dateToStart.setHours(Number(data.time.substring(0, 2)));
            dateToStart.setMinutes(Number(data.time.substring(3, 5)));
            $scope.start = formatDate(dateToStart) + " в " + data.time.substring(0, 5);


            //created date
            var createddate = new Date(data.created_at);
            $scope.created_at = formatDate(createddate) + " в " + formatTime(createddate);

            //close date
            var closedate = new Date(dateToStart);
            closedate.setMinutes(closedate.getMinutes() - 10);//Registration closes 10 minutes before the start
            $scope.close_at = formatTime(closedate);
            $scope.close_position = calcPositionOnGraph(createddate, dateToStart, closedate);

            //register date
            var registerdate = new Date(dateToStart);
            registerdate.setHours(registerdate.getHours() - 6);//Confirmation of registration begins 3 hours before the start
            if (registerdate < createddate) registerdate = createddate;//if register under the created time, then equals them
            $scope.register_at = formatTime(registerdate);
            $scope.register_position = calcPositionOnGraph(createddate, dateToStart, registerdate);

            //now
            $scope.now_position = calcPositionOnGraph(createddate, dateToStart, new Date());
        }

        var tournament_id = $stateParams['tournament_id'];

        //// REST requests ////
        function doQuery() {
            var d = $q.defer();
            var result = tournamentById.query({id: tournament_id}, function () {
                d.resolve(result);
            });
            return d.promise;
        }

        var promise = doQuery();

        promise.then(function (data) {
            console.log("Success");
            console.log(data);
            if (!data.background) //default background
                data.background = "/static/assets/img/img551f2216e17ef.jpg";
            $scope.tournamentData = data;
            $scope.logs = data.log_manager.log_messages;
            $scope.logs.forEach(function(elem, index, array) {
                var d = new Date(elem.created_at);
                elem.created_at = formatDate(d) + ", " + formatTime(d);
            });
            calcDatesForGraph(data);
        });

        attendantsByTournamentId.query({id: tournament_id}, function (data) {
            console.log("Success");
            console.log(data);
            $scope.attendantsData = data;


            djangoAuth.profile().then(function (data) {
                console.log("SUCCEED GET USER PROFILE");
                console.log(data);

                for (var j = 0; j < $scope.attendantsData.length; j++) {
                    if ($scope.attendantsData[j].id == data.id) {
                        $scope.isAlreadyAttendant = true;
                        break;
                    }
                }
            });
        }, function (data) {
            console.log("Failed");
            console.log(data);
        });

        //// END REST requests ////


        timer = $interval(function () {
            if (dateToStart != null) {
                $scope.diff = calcDiff(dateToStart, new Date());
            }
        }, 500);


        $scope.$on('$destroy', function () {
            if (angular.isDefined(timer)) {
                $interval.cancel(timer);
                timer = undefined;
            }
        });

        $scope.addAttendant = function () {
            var request = {
                "tournament_id": $stateParams['tournament_id']
            };
            attendants.save(request, function (data) {
                console.log("SUCCESS");
                console.log(data);
                $scope.isAlreadyAttendant = true;
                $scope.attendantsData.push(data);
                console.log($scope.attendantsData);
            }, function (data) {
                console.log("FAILED");
                console.log(data);
            })
        };


        //// TOURNAMENT BRACKET TAB //////

        // data object for bracket controller
        $scope.bracketData = {
            teams: [],
            tournament: {
                type: "SE",
                matches: []
            },
            options: {
                //onTeamRightClick: showSelectTeam,
                //onTeamClick: $scope.onTeamClick,
                //onMatchClick: showDetails,
                //onMatchRightClick: $scope.onMatchRightClick
            }
        };

        function startTournament(td, teams) {
            $scope.bracketData.teams = teams;
            $scope.bracketData.tournament = td;
            if(!$scope.isNotStarted && !$scope.isCanceled)
                $scope.bracketData.reload();
        }

        var td = null;
        var participants;
        participants = tournamentAttendantsById.query({id: $stateParams['tournament_id']}, function () {
            participants = "[" + JSON.stringify(participants) + "]";
            $scope.at = participants;
            console.log(attendants);

            td = tournamentDataById.query({id: $stateParams['tournament_id']}, function () {
                if (td.properties.status == 'Not started')
                    $scope.isNotStarted = true;
                if (td.properties.status == 'Canceled')
                    $scope.isCanceled = true;
                startTournament(td, JSON.parse(participants));
                $scope.td = td;
                console.log(td);
            });
        });






        //// END OF TOURNAMENT BRACKET TAB //////

    }])
;