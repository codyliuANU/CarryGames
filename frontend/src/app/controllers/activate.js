// activate controller
app.controller('ActivateController', ['$scope', 'djangoAuth', '$state', '$stateParams',
    function ($scope, djangoAuth, $state, $stateParams) {
        djangoAuth.activate($stateParams.uid, $stateParams.token)
            .then(function (data) {
                //success case
                console.info("success activation");
                $state.go('access.signin');
            }, function (data) {
                console.log(data);
                $scope.errors = data;
            });
    }])
;