

// new tournament form controller
app.controller('NewTournamentFormController', ['$scope', 'djangoAuth', '$state', function($scope, djangoAuth, $state) {
    $scope.tournament = {'name':'', 'type':'',
        'allmatches':'',
        'semi':'',
        'finals':'',
        'maxplayers':'6',
        'rules':'',
        'date':'',
        'time':'',
        'fare':'0'
    };
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