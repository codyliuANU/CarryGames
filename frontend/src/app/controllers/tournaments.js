/* Controllers */
// tournaments (main page) controller
app.controller('TournamentsController', ['$scope', 'tournaments',
    function ($scope, tournaments) {

        function formatDate(d){
            var monthNames = [
                "Января", "Февраля", "Марта",
                "Апреля", "Мая", "Июня", "Июля",
                "Августа", "Сентября", "Октября",
                "Ноября", "Декабря"
            ];

            var day = d.getDate();
            var monthIndex = d.getMonth();

            return day + " " + monthNames[monthIndex] ;
        }

        var ts = tournaments.query(function(data) {
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
        });
}])
;