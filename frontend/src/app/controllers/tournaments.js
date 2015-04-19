/* Controllers */
// tournaments (main page) controller
app.controller('TournamentsController', ['$scope', 'tournaments',
    function ($scope, tournaments) {
        var ts = tournaments.query(function(data) {
            // Transform object into array
            var data_array =[];
            for( var i in data ) {
                if (typeof data[i] === 'object' && data[i].hasOwnProperty("name")){
                    data_array.push(data[i]);
                }
            }
            // Chunk Array and apply scope
            $scope.tournaments = data_array.chunk(3);
            console.log($scope.tournaments);
        });
}])
;