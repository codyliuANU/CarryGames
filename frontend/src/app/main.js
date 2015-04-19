/* Controllers */

angular.module('app')
    .controller('AppCtrl', ['$scope', '$translate', '$localStorage', '$window', 'djangoAuth', '$state',
        function ($scope, $translate, $localStorage, $window, djangoAuth, $state) {
            // add 'ie' classes to html
            var isIE = !!navigator.userAgent.match(/MSIE/i);
            isIE && angular.element($window.document.body).addClass('ie');
            isSmartDevice($window) && angular.element($window.document.body).addClass('smart');

            // config
            $scope.app = {
                name: 'CarryGames',
                version: '0.0.1',
                host: 'localhost:8080',
                // for chart colors
                color: {
                    primary: '#7266ba',
                    info: '#23b7e5',
                    success: '#27c24c',
                    warning: '#fad733',
                    danger: '#f05050',
                    light: '#e8eff0',
                    dark: '#3a3f51',
                    black: '#1c2b36'
                },
                settings: {
                    themeID: 1,
                    navbarHeaderColor: 'bg-black',
                    navbarCollapseColor: 'bg-white-only',
                    asideColor: 'bg-black',
                    headerFixed: true,
                    asideFixed: false,
                    asideFolded: false,
                    asideDock: false,
                    container: false
                }
            }

            // save settings to local storage
            if (angular.isDefined($localStorage.settings)) {
                $scope.app.settings = $localStorage.settings;
            } else {
                $localStorage.settings = $scope.app.settings;
            }
            $scope.$watch('app.settings', function () {
                if ($scope.app.settings.asideDock && $scope.app.settings.asideFixed) {
                    // aside dock and fixed must set the header fixed.
                    $scope.app.settings.headerFixed = true;
                }
                // save to local storage
                $localStorage.settings = $scope.app.settings;
            }, true);

            // angular translate
            $scope.lang = {isopen: false};
            $scope.langs = {en: 'English', de_DE: 'German', it_IT: 'Italian'};
            $scope.selectLang = $scope.langs[$translate.proposedLanguage()] || "English";
            $scope.setLang = function (langKey, $event) {
                // set the current lang
                $scope.selectLang = $scope.langs[langKey];
                // You can change the language during runtime
                $translate.use(langKey);
                $scope.lang.isopen = !$scope.lang.isopen;
            };

            console.log("controller ON");

            // Assume user is not logged in until we hear otherwise
            $scope.authenticated = false;

            // Wait for the status of authentication, set scope var to true if it resolves
            djangoAuth.authenticationStatus(true).then(function () {
                $scope.authenticated = true;
                djangoAuth.profile().then(function (data) {
                    $scope.account = data;
                })
            });

            // catch login(out) notifications
            // Wait and respond to the logout event.
            $scope.$on('djangoAuth.logged_out', function () {
                console.info("logout");
                $scope.authenticated = false;
                delete $scope.account;
            });
            // Wait and respond to the log in event.
            $scope.$on('djangoAuth.logged_in', function () {
                console.info("login");
                $scope.authenticated = true;
                djangoAuth.profile().then(function (data) {
                    $scope.account = data;
                })
            });

            $scope.logout = function () {
                djangoAuth.logout()
                    .then(function (data) {
                        //success case
                        console.log("logged out successfully");
                        $state.go("app.dashboard-v1");
                    }, function (data) {
                        console.log("logout error: " + data);
                    });
            };

            function isSmartDevice($window) {
                // Adapted from http://www.detectmobilebrowsers.com
                var ua = $window['navigator']['userAgent'] || $window['navigator']['vendor'] || $window['opera'];
                // Checks for iOs, Android, Blackberry, Opera Mini, and Windows mobile devices
                return (/iPhone|iPod|iPad|Silk|Android|BlackBerry|Opera Mini|IEMobile/).test(ua);
            }

        }]);