/**
 * Created by la0rg on 5/31/15.
 */
app.controller('SigninBNetController', ['$scope', '$http', '$state', 'djangoAuth', 'AuthToken',
    function ($scope, $http, $state, djangoAuth, AuthToken) {
        $scope.authError = null;

        $scope.login = function () {
            var client_id="pkbcgy8h99jyhmwvwq9rt9ysqvg5mze7";
            var redirect_uri="https://127.0.0.1:8000/authcode/";
            var response_type="code";
            var token = AuthToken.generateNewToken();
            console.log(token);

            var url="https://eu.battle.net/oauth/authorize?response_type="+response_type+"&client_id="+client_id+
                "&redirect_uri="+redirect_uri+"&state="+token;
            window.location.replace(url);
        };
    }])
;