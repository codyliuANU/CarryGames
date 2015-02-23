/* global angular */
angular.module( 'ngBoilerplate', [
  'templates-app',
  'templates-common',
  'ngBoilerplate.home',
  'ngBoilerplate.about',
  'ui.router',
  'ngCookies'
])

/**
 * This configures the root route
 * @param  {Object} $stateProvider     The state provider
 * @param  {Object} $urlRouterProvider The URL provider
 */
.config( function myAppConfig ( $stateProvider, $urlRouterProvider ) {
  $urlRouterProvider.otherwise( '/home' );
})

.run( function run ($http, $cookies) {
  // For CSRF token compatibility with Django
  $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
})

.controller( 'AppCtrl', function AppCtrl ( $scope ) {
  $scope.$on('$stateChangeSuccess', function(event, toState){
    if ( angular.isDefined( toState.data.pageTitle ) ) {
      $scope.pageTitle = toState.data.pageTitle + ' | ngBoilerplate' ;
    }
  });
})

;
