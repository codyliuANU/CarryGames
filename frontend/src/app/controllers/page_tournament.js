/* Controllers */
// tournaments (main page) controller
app.controller('PageTournamentController', ['$scope', 'tournamentById', '$stateParams', '$q', '$interval',
    function ($scope, tournamentById, $stateParams, $q, $interval) {

        function formatDate(d){
            var day = d.getDate();
            var monthIndex = d.getMonth();

            if(day < 10) day = "0" + day;
            if(monthIndex < 10) monthIndex = "0" + monthIndex;

            return day + "." + monthIndex;
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
            dateToStart = new Date(data.date);
            $scope.start = formatDate(dateToStart) + " в " + data.time.substring(0, 5);
            console.log("start");
            console.log($scope.start);
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