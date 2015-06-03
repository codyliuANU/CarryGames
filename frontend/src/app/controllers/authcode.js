/**
 * Created by la0rg on 6/1/15.
 */
app.controller('AuthCodeController', ['AuthToken', '$stateParams', 'djangoAuth', '$state', '$scope',
    function (AuthToken, $stateParams, djangoAuth, $state, $scope) {
        var code = $stateParams.code;
        console.log("CODE!!");
        console.log(code);
        console.log($stateParams.state);
        if(AuthToken.isEqualsToAuthToken($stateParams.state)){
            djangoAuth.loginByAuthCode(code)
                .then(function (data) {
                    //success case
                    console.log("logged in successfully");
                    $state.go('app.tournaments.all');
                }, function (data) {
                    console.log(data);
                    $scope.authError = data;
                });
        }
    }])
;