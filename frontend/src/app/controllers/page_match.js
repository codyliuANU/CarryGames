/* Controllers */
// tournaments (main page) controller
app.controller('PageMatchController', ['$scope', 'matchById', '$stateParams',
    function ($scope, matchById, $stateParams) {

        console.log($stateParams['match_id']);

        $scope.results = [];
        $scope.miss = false;
        $scope.violation = false;

        matchById.query({id: $stateParams['match_id']}, function (data) {
            $scope.match = data;
            for(var i = 0; i < parseInt(data.mode[2]); i++){
                var fight = {model: 'radio' + i,
                             value: '-'};
                $scope.results.push(fight);
            }
            console.log($scope.match);
        }, function () {
            console.log("Problem with getting match data.")
        });

        $scope.sendResult = function () {

        }

    }])
;