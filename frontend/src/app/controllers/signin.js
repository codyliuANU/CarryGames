/* Controllers */
// signin controller
app.controller('SigninFormController', ['$scope', '$http', '$state', 'djangoAuth',
    function ($scope, $http, $state, djangoAuth) {
        $scope.authError = null;

        $scope.login = function () {
            djangoAuth.login($scope.model.battle_tag, $scope.model.password)
                .then(function (data) {
                    //success case
                    console.log("logged in successfully");
                    $state.go('app.dashboard-v1');
                }, function (data) {
                    console.log(data);
                    $scope.authError = data;
                });
        };
    }])
;