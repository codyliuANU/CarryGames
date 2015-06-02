// config

angular.module('app')
    .config(
    ['$controllerProvider', '$compileProvider', '$filterProvider', '$provide',
        function ($controllerProvider, $compileProvider, $filterProvider, $provide) {

            // lazy controller, directive and service
            app.controller = $controllerProvider.register;
            app.directive = $compileProvider.directive;
            app.filter = $filterProvider.register;
            app.factory = $provide.factory;
            app.service = $provide.service;
            app.constant = $provide.constant;
            app.value = $provide.value;

           /* $provide.decorator('$sniffer', function($delegate) {
                $delegate.history = false;
                return $delegate;
            });*/
        }
    ])
    .config(['$translateProvider', function ($translateProvider) {
        // Register a loader for the static files
        // So, the module will search missing translation tables under the specified urls.
        // Those urls are [prefix][langKey][suffix].
        $translateProvider.useStaticFilesLoader({
            prefix: 'static/assets/l10n/',
            suffix: '.js'
        });
        // Tell the module what language to use by default
        $translateProvider.preferredLanguage('en');
        // Tell the module to store the language in the local storage
        $translateProvider.useLocalStorage();
    }])
    .config(function ($locationProvider) {
        $locationProvider.html5Mode(true);
    })
    .config(['OAuthProvider', function(OAuthProvider) {
        OAuthProvider.configure({
            baseUrl: 'https://eu.battle.net/oauth/authorize',
            clientId: 'pkbcgy8h99jyhmwvwq9rt9ysqvg5mze7',
            clientSecret: '7EqzYtxB427Yb4AAfB3PR2bjMT4vxTwd'
        });
    }]);