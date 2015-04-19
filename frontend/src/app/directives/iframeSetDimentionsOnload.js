angular.module('app')
    .directive('iframeSetDimentionsOnload', [function () {
        return {
            restrict: 'A',
            link: function (scope, element, attrs) {
                element.on('load', function () {
                    /* Set the dimensions here,
                     I think that you were trying to do something like this: */
                    console.log(element.prev());
                    var otherHeight = $(element.prev()).outerHeight(true);
                    $(window).resize(function() {
                        $('.iframe').height( $(window).height() - otherHeight );
                    }).resize();
                    /*var iFrameHeight = element[0].offsetHeight + 'px';
                    var iFrameWidth = '100%';
                    console.log(iFrameHeight);
                    element.css('width', iFrameWidth);
                    element.css('height', iFrameHeight);*/
                })
            }
        }
    }])
    .directive('myIframe', function () {
        var linkFn = function (scope, element, attrs) {
            element.find('iframe').bind('load', function (event) {
                event.target.contentWindow.scrollTo(0, 400);
            });
        };
        return {
            restrict: 'EA',
            scope: {
                src: '&src',
                height: '@height',
                width: '@width',
                scrolling: '@scrolling'
            },
            template: '<iframe class="frame" height="{{height}}" width="{{width}}" frameborder="0" border="0" marginwidth="0" marginheight="0" scrolling="{{scrolling}}" src="{{src()}}"></iframe>',
            link: linkFn
        };
    });