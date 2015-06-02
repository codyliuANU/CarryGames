/**
 * Created by la0rg on 6/1/15.
 */
angular.module('AuthTokenModule', [])
  .factory('AuthToken', function ($cookies) {
        return {
            getAuthToken: function() {return $cookies.auth_token_cg;},
            generateNewToken: function() {
                var token = Math.random().toString(36).substring(2,9);
                $cookies.auth_token_cg = token;
                return token;
            },
            isEqualsToAuthToken: function(s) {
                return s==$cookies.auth_token_cg;
            }
        };
    }
);