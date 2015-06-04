// new tournament form controller
app.controller('NewTournamentFormController', ['$scope', 'tournaments', '$state', 'FileUploader', '$cookies','toaster',
    function ($scope, tournaments, $state, FileUploader, $cookies, toaster) {
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
            'fare': '0',
            'region': ''
        };

        $scope.time = new Date();
        $scope.date = new Date();

        function showPopUp(title, message, isSuccess) {
            if (isSuccess)
                toaster.pop('success', title, message);
            else
                toaster.pop('error', title, message);
        };



        $scope.alerts = [];

        var token = 'Token ';
        if ($cookies.token) {
            token += $cookies.token;
        }

        $scope.uploader = new FileUploader({
            url: '/api-v1/tournaments/',
            alias: 'background',
            method: 'POST',
            headers: {
                'Authorization': token
            }
        });
        // FILTERS

        $scope.uploader.filters.push({
            name: 'imageFilter',
            fn: function (item /*{File|FileLikeObject}*/, options) {
                var type = '|' + item.type.slice(item.type.lastIndexOf('/') + 1) + '|';
                if ('|jpg|png|jpeg|'.indexOf(type) !== -1) {
                    $scope.uploader.clearQueue();
                    $scope.alerts = [];
                    return true;
                } else return false;
            }
        });


        // CALLBACKS

        $scope.uploader.onWhenAddingFileFailed = function (item /*{File|FileLikeObject}*/, filter, options) {
            console.info('onWhenAddingFileFailed', item, filter, options);
            $scope.alerts.push({
                type: 'danger',
                msg: 'Произошла ошибка при выборе файла. Можно использовать только jpg и png.'
            });
        };


        $scope.uploader.onBeforeUploadItem = function (item) {
            console.info('onBeforeUploadItem', item);
            item.formData.push($scope.tournament);
        };
        $scope.uploader.onSuccessItem = function (fileItem, response, status, headers) {
            $state.go('app.tournaments.id', {tournament_id: response.id});
        };
        $scope.uploader.onErrorItem = function (fileItem, response, status, headers) {
            showPopUp('Создание турнира', 'Произошла ошибка.' + response.data, false);
        };

        $scope.closeAlert = function (index) {
            $scope.alerts.splice(index, 1);
        };

        $scope.create = function () {

            console.log("call create");
            //time format
            var t = $scope.time;
            $scope.tournament.time = t.getHours() + ":" + t.getMinutes();
            //date format
            var t = $scope.date;
            $scope.tournament.date = t.getFullYear() + "-" + (t.getMonth() + 1) + "-" + t.getDate();

            if ($scope.uploader.queue.length > 0) {
                console.log("uploadItem");
                $scope.uploader.uploadItem(0);
            }
            else {
                console.log("use service");
                $scope.tournament.background = null;
                tournaments.save($scope.tournament, function (data) {
                    console.log("SUCCESS");
                    $state.go('app.tournaments.id', {tournament_id: data.id});
                }, function (data) {
                    console.log("FAILED");
                    showPopUp('Создание турнира', 'Произошла ошибка.' + data.data, false);
                })
            }
        };
    }])
;