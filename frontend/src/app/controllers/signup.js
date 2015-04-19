

// signup controller
app.controller('SignupFormController', ['$scope', 'djangoAuth', '$state', function($scope, djangoAuth, $state) {
    $scope.model = {'battle_tag':'', 'password':'', 'email':''};
    $scope.result = false;

    $scope.signup = function() {
      djangoAuth.register($scope.model.battle_tag,$scope.model.password,$scope.model.email)
      .then(function(data) {
            //success case
            $scope.result = true;
            //$state.go('app.dashboard-v1');
      }, function (data) {
              console.log(data);
            $scope.errors = data;
      });
    };
  }])
 ;