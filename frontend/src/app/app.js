/* global angular */
var app = angular.module('app', [
        'templates-app',
        'templates-common',
        'ui.router',
        'ngCookies',
        'ngAnimate',
        'ngResource',
        'ngSanitize',
        'ngTouch',
        'ngStorage',
        'ui.bootstrap',
        'ui.load',
        'ui.jq',
        'ui.validate',
        'oc.lazyLoad',
        'pascalprecht.translate',
        'djangoAuthModule',
        'djangoTournamentModule',
        'ngBracket'
    ])

    /**
     * This configures the root route
     * @param  {Object} $stateProvider     The state provider
     * @param  {Object} $urlRouterProvider The URL provider
     */
        /*.config( function myAppConfig ( $stateProvider, $urlRouterProvider ) {
         $urlRouterProvider.otherwise( '/home' );
         })*/

        .run(function run($http, $cookies, $log, djangoAuth) {
            // For CSRF token compatibility with Django
            //$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
            djangoAuth.initialize('//127.0.0.1:8080/api/auth', false);
        })

/*.controller( 'AppCtrl', function AppCtrl ( $scope ) {
 $scope.$on('$stateChangeSuccess', function(event, toState){
 if ( angular.isDefined( toState.data.pageTitle ) ) {
 $scope.pageTitle = toState.data.pageTitle + ' | ngBoilerplate' ;
 }
 });
 })*/

    ;
