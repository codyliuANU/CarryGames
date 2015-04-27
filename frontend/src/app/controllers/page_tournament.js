/* Controllers */
// tournaments (main page) controller
app.controller('PageTournamentController', ['$scope', 'tournamentById', '$stateParams', '$q', '$interval',
    function ($scope, tournamentById, $stateParams, $q, $interval) {


        $scope.start = '';
        $scope.created_at = '';
        $scope.close_at = '';
        $scope.register_at = '';
        $scope.now_position = 0;


        function formatDate(d){
            var day = d.getDate();
            var monthIndex = d.getMonth() + 1;

            if(day < 10) day = "0" + day;
            if(monthIndex < 10) monthIndex = "0" + monthIndex;

            return day + "." + monthIndex;
        }

        function formatTime(d){
            var hours = d.getHours();
            var minutes = d.getMinutes();

            if(hours < 10) hours = "0" + hours;
            if(minutes < 10) minutes = "0" + minutes;

            return hours + ":" + minutes;
        }

        function calcDiff(d1, d2) {
            var diff=d2-d1,sign=diff<0?-1:1,milliseconds,seconds,minutes,hours,days;
            diff/=sign; // or diff=Math.abs(diff);
            diff=(diff-(milliseconds=diff%1000))/1000;
            diff=(diff-(seconds=diff%60))/60;
            diff=(diff-(minutes=diff%60))/60;
            days=(diff-(hours=diff%24))/24;
            return days + " дней, " + hours + " часов, " + minutes + " минут, " + seconds + " секунд."
        }

        function calcPositionOnGraph(created, start, value){
            var x1 = 25;//created_at - x coordinate
            var x2 = 499;//date(start) - x coordinate

            var total = start - created;
            var progress = value - created;
            var percent = progress/ total;
            return (x2 - x1) * percent + x1;
        }


        function calcDatesForGraph(data){
            //start date
            var dateToStart = new Date(data.date);
            dateToStart.setHours(Number(data.time.substring(0,2)));
            dateToStart.setMinutes(Number(data.time.substring(3,5)));
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
            if(registerdate < createddate) registerdate = createddate;//if register under the created time, then equals them
            $scope.register_at = formatTime(registerdate);
            $scope.register_position = calcPositionOnGraph(createddate, dateToStart, registerdate);

            //now
            $scope.now_position = calcPositionOnGraph(createddate, dateToStart, new Date());
        }

        var tournament_id = $stateParams['tournament_id'];

        function doQuery() {
            var d = $q.defer();
            var result = tournamentById.query({id:tournament_id}, function() {
                d.resolve(result);
            });
            return d.promise;
        }

        var promise = doQuery();

        var dateToStart = null;
        promise.then(function(data) {
            console.log("Success");
            console.log(data);
            if(!data.background) //default background
                data.background = "/static/assets/img/img551f2216e17ef.jpg";
            $scope.tournamentData = data;
            calcDatesForGraph(data);
        });


        timer = $interval(function() {
            if(dateToStart != null){
                $scope.diff = calcDiff(dateToStart, new Date());
            }
        }, 500);




        $scope.$on('$destroy', function() {
          if (angular.isDefined(timer)) {
            $interval.cancel(timer);
            timer = undefined;
          }
        });
        /*var ts = tournaments.query(function(data) {
            // Transform object into array
            var data_array =[];
            for( var i in data ) {
                if (typeof data[i] === 'object' && data[i].hasOwnProperty("name")){
                    data[i].date = formatDate(new Date(data[i].date));
                    data[i].time = data[i].time.substring(0, 5);
                    data_array.push(data[i]);
                }
            }
            // Chunk Array and apply scope
            $scope.tournaments = data_array.chunk(3);
            console.log($scope.tournaments);
        });*/
}])
;