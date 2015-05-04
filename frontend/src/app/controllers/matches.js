/* Controllers */
// tournaments (main page) controller
app.controller('MatchesController', ['$scope', 'matches', '$state',
    function ($scope, matches, $state) {

        matches.query(function (data) {
            $scope.matches = data;

            if($state.is('app.matches.my')){
                $scope.matches = $scope.matches.filter(function (x) {
                    if(x.contestant1.account.id == $scope.account.id || $scope.account.id == x.contestant2.account.id)
                        return x
                });
            }

            console.log($scope.matches);
        }, function () {
            console.log("Problem with getting matches data.")
        });

    }])
;