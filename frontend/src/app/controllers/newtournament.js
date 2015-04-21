// new tournament form controller
app.controller('NewTournamentFormController', ['$scope', 'tournaments', '$state', 'FileUploader', function ($scope, tournaments, $state, FileUploader) {
    $scope.tournament = {
        'name': '',
        'format': '',
        'allmatches': '',
        'semi': '',
        'finals': '',
        'maxplayers': '6',
        'rules': '',
        'date': '',
        'time': '',
        'fare': '0'
    };

    $scope.alerts = [];

    $scope.uploader = new FileUploader({
        url:'/api-v1/tournaments/',
        alias: 'background',
        method: 'POST'
    });
    // FILTERS

    $scope.uploader.filters.push({
        name: 'imageFilter',
        fn: function (item /*{File|FileLikeObject}*/, options) {
            var type = '|' + item.type.slice(item.type.lastIndexOf('/') + 1) + '|';
            if('|jpg|png|jpeg|'.indexOf(type) !== -1){
                $scope.uploader.clearQueue();
                $scope.alerts = [];
                return true;
            } else return false;
        }
    });


    // CALLBACKS

        $scope.uploader.onWhenAddingFileFailed = function(item /*{File|FileLikeObject}*/, filter, options) {
            console.info('onWhenAddingFileFailed', item, filter, options);
            $scope.alerts.push({type: 'danger', msg: 'Произошла ошибка при выборе файла. Можно использовать только jpg и png.'});
        };
        $scope.uploader.onAfterAddingFile = function(fileItem) {
            console.info('onAfterAddingFile', fileItem);
        };
        $scope.uploader.onAfterAddingAll = function(addedFileItems) {
            console.info('onAfterAddingAll', addedFileItems);
        };
        $scope.uploader.onBeforeUploadItem = function(item) {
            console.info('onBeforeUploadItem', item);
            item.formData.push($scope.tournament);
        };
        $scope.uploader.onProgressItem = function(fileItem, progress) {
            console.info('onProgressItem', fileItem, progress);
        };
        $scope.uploader.onProgressAll = function(progress) {
            console.info('onProgressAll', progress);
        };
        $scope.uploader.onSuccessItem = function(fileItem, response, status, headers) {
            console.info('onSuccessItem', fileItem, response, status, headers);
        };
        $scope.uploader.onErrorItem = function(fileItem, response, status, headers) {
            console.info('onErrorItem', fileItem, response, status, headers);
        };
        $scope.uploader.onCancelItem = function(fileItem, response, status, headers) {
            console.info('onCancelItem', fileItem, response, status, headers);
        };
        $scope.uploader.onCompleteItem = function(fileItem, response, status, headers) {
            console.info('onCompleteItem', fileItem, response, status, headers);
        };
        $scope.uploader.onCompleteAll = function() {
            console.info('onCompleteAll');
        };

    $scope.closeAlert = function(index) {
      $scope.alerts.splice(index, 1);
    };


    $scope.create = function () {

         console.log("call create");
         //time format
         var t = $scope.tournament.time;
         $scope.tournament.time = t.getHours() + ":" + t.getMinutes();
         //date format
         var t = $scope.tournament.date;
         $scope.tournament.date = t.getFullYear() + "-" + (t.getMonth() + 1) +"-" +t.getDate();

        if($scope.uploader.length >= 0) {
            console.log("uploadItem");
            $scope.uploader.uploadItem(0);
        }
        else {
            console.log("use service");
            $scope.tournament.background = null;
            tournaments.save($scope.tournament, function(data) {
                console.log("SUCCESS");
                console.log(data);
            }, function (data) {
                console.log("FAILED");
                console.log(data);
            })
        }


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