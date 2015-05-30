/* Controllers */
// tournaments (main page) controller
app.controller('PageMatchController', ['$scope', 'matchById', '$stateParams', 'djangoAuth', 'toaster', '$q',
    function ($scope, matchById, $stateParams, djangoAuth, toaster, $q) {

        console.log($stateParams['match_id']);

        $scope.btns = {model: ""};
        $scope.miss = false;
        $scope.violation = false;
        $scope.isManagerResult = false;
        $scope.isAvailableToSetValue = false;
        $scope.isUserBelongToThisMatch = false;
        $scope.refreshclass = "";


        //TODO: These funcitons is duplicated from page_tournament.js. Consider how to extract them to a one file.
        function formatDate(d) {
            var day = d.getDate();
            var monthIndex = d.getMonth() + 1;

            if (day < 10) day = "0" + day;
            if (monthIndex < 10) monthIndex = "0" + monthIndex;

            return day + "." + monthIndex;
        }

        function formatTime(d) {
            var hours = d.getHours();
            var minutes = d.getMinutes();

            if (hours < 10) hours = "0" + hours;
            if (minutes < 10) minutes = "0" + minutes;

            return hours + ":" + minutes;
        }
        // END OF TODO


        function showPopUp(title, message, isSuccess) {
            if (isSuccess)
                toaster.pop('success', title, message);
            else
                toaster.pop('error', title, message);
        };


        function isManager() {
            var d = $q.defer();
            if ($scope.match.status == 'Created' || $scope.match.status == 'In progress') {
                djangoAuth.profile().then(function (data) {
                    d.resolve(data);
                    if (data != null) {
                        if (data.id == $scope.match.contestant1.account.id || data.id == $scope.match.contestant2.account.id)
                            $scope.isManagerResult = true;
                        else
                            $scope.isManagerResult = false;
                    } else
                        $scope.isManagerResult = false;
                });
            } else {
                d.resolve();
                $scope.isManagerResult = false;
            }
            return d.promise;
        }

        function isAvailableToSetValue() {
            var d = $q.defer();
            djangoAuth.profile().then(function (data) {
                d.resolve(data);
                if (data != null) {
                    if (data.id == $scope.match.contestant1.account.id && $scope.match.result_user1 == null)
                        $scope.isAvailableToSetValue = true;
                    else if (data.id == $scope.match.contestant2.account.id && $scope.match.result_user2 == null)
                        $scope.isAvailableToSetValue = true;
                    else
                        $scope.isAvailableToSetValue = false;
                } else
                    $scope.isAvailableToSetValue = false;
            });
            return d.promise;
        }

        function isUserBelongToThisMatch() {
            var d = $q.defer();
            djangoAuth.profile().then(function (data) {
                d.resolve(data);
                if (data != null) {
                    if (data.id == $scope.match.contestant1.account.id)
                        $scope.isUserBelongToThisMatch = true;
                    if (data.id == $scope.match.contestant2.account.id)
                        $scope.isUserBelongToThisMatch = true;
                }
            });
            return d.promise;
        }

        function startUp() {
            var d = $q.defer();
            var result = matchById.query({id: $stateParams['match_id']}, function (data) {
                $scope.match = data;
                console.log($scope.match);

                $scope.logs = data.log_manager.log_messages;
                $scope.logs.forEach(function (elem, index, array) {
                    var d = new Date(elem.created_at);
                    elem.created_at = formatDate(d) + ", " + formatTime(d);
                });

                var p1 = isManager();
                var p2 = isAvailableToSetValue();
                var p3 = isUserBelongToThisMatch();

                $q.all([p1, p2, p3]).then(function () {
                    d.resolve(result);
                });
            }, function (data) {
                showPopUp('Ошибка обновления', "Невозможно получить данные матча: " + data.data, false);
                d.resolve(result);
            });
            return d.promise;
        }

        startUp();

        $scope.sendResult = function () {
            console.log($scope.results);
            if (!$scope.violation && !$scope.miss) {
                var data = {
                    id: $stateParams['match_id'],
                    value_to_setup: $scope.btns.model
                };
                matchById.setValue(data, function (data) {
                    console.log("OK!");
                    $scope.match = data;
                    isManager();
                    isAvailableToSetValue();
                    console.log(data);
                    $scope.btns.model = "-";
                    showPopUp('Отправка результата боя', 'Ваши данные отправлены успешно, ожидайте ответ от соперника.', true);
                }, function (data) {
                    console.log(data);
                    isManager();
                    isAvailableToSetValue();
                    showPopUp('Отправка результата боя', 'Во время отправки данных прозошла ошибка.' + data.data, false);
                });
            }
        }

        $scope.refresh = function () {
            $scope.refreshclass = "fa-spin";
            var startUp_promise = startUp();
            startUp_promise.then(function (data) {
                $scope.refreshclass = "";
            }, function () {
                $scope.refreshclass = "";
            });
        }

    }])
;