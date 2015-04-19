

// new tournament form controller
app.controller('NewTournamentFormController', ['$scope', 'tournaments', '$state', function($scope, tournaments, $state) {
    $scope.tournament = {
        'name':'',
        'format':'',
        'allmatches':'',
        'semi':'',
        'finals':'',
        'maxplayers':'6',
        'rules':'',
        'date':'',
        'time':'',
        'fare':'0',
        'background':''
    };

    $scope.create = function() {
       /* console.log("call create");
        //time format
        var t = $scope.tournament.time;
        $scope.tournament.time = t.getHours() + ":" + t.getMinutes();
        //date format
        var t = $scope.tournament.date;
        $scope.tournament.date = t.getFullYear() + "-" + (t.getMonth() + 1) +"-" +t.getDate();

      tournaments.save($scope.tournament, function(data) {
          console.log("result");
          console.log(data);
      }), function(error) {
          console.log("exception");
          console.log(error);
      }*/

       /* var fd = new FormData();
        _.each($scope.tournament, function (val, key) {
            fd.append(key, data[key]);
        });

        $http({
            method: 'POST',
            url: '/api-v1/attendants/',
            data: fd,
            transformRequest: angular.identity,
            headers: {
                'Content-Type': undefined
            }
        })
        .success(function (response) {
            console.log("success");
            console.log(response);
        })
        .error(function (error) {
            console.log("error");
            console.log(error);
        }); */
    };
  }])
 ;