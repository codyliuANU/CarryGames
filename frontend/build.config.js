/**
 * This file/module contains all configuration for the build process.
 */
module.exports = {
  /**
   * The `build_dir` folder is where our projects are compiled during
   * development and the `compile_dir` folder is where our app resides once it's
   * completely built.
   */
  build_dir: 'build',
  compile_dir: 'bin',

  /**
   * This is a collection of file patterns that refer to our app code (the
   * stuff in `src/`). These file paths are used in the configuration of
   * build tasks. `js` is all project javascript, less tests. `ctpl` contains
   * our reusable components' (`src/common`) template HTML files, while
   * `atpl` contains the same, but for our app's code. `html` is just our
   * main HTML file, `less` is our main stylesheet, and `unit` contains our
   * app's unit tests.
   */
  app_files: {
    js: [ 'src/app/**/*.js', '!src/app/**/*.spec.js'],
    jsunit: [ 'src/app/*.spec.js' ],

    coffee: [ 'src/app/*.coffee', '!src/app/*.spec.coffee' ],
    coffeeunit: [ 'src/app/*.spec.coffee' ],

    atpl: [ 'src/app/**/*.tpl.html', 'src/app/**/*.html' ],
    ctpl: [ 'src/common/**/*.tpl.html' ],

    html: [ 'src/index.html' ],
    less: 'src/less/anglr.less'
  },

  /**
   * This is a collection of files used during testing only.
   */
  test_files: {
    js: [
      'vendor/angular-mocks/angular-mocks.js'
    ]
  },


  /**
   * This is the same as `app_files`, except it contains patterns that
   * reference vendor code (`vendor/`) that we need to place into the build
   * process somewhere. While the `app_files` property ensures all
   * standardized files are collected for compilation, it is the user's job
   * to ensure non-standardized (i.e. vendor-related) files are handled
   * appropriately in `vendor_files.js`.
   *
   * The `vendor_files.js` property holds files to be automatically
   * concatenated and minified with our project source files.
   *
   * The `vendor_files.css` property holds any CSS files to be automatically
   * included in our app.
   *
   * The `vendor_files.assets` property holds any assets to be copied along
   * with our app's assets. This structure is flattened, so it is not
   * recommended that you use wildcards.
   */
  vendor_files: {
    js: [
       'vendor/jquery/jquery.min.js',
        'vendor/jquery/jquery.min.map',
      'vendor/angular/angular.js',
      'vendor/angular-bootstrap/ui-bootstrap-tpls.min.js',
      'vendor/placeholders/angular-placeholders-0.0.1-SNAPSHOT.min.js',
      'vendor/angular-ui-router/release/angular-ui-router.js',
      'vendor/angular-ui-utils/ui-utils.js',
      'vendor/angular-cookies/angular-cookies.min.js',
      'vendor/angular-django-rest-resource/angular-django-rest-resource.js',
        'vendor/angular-animate/angular-animate.js',
        'vendor/angular-resource/angular-resource.js',
         'vendor/angular-sanitize/angular-sanitize.js',
        'vendor/angular-touch/angular-touch.js',
        'vendor/ngstorage/ngStorage.js',
        'vendor/oclazyload/dist/ocLazyLoad.js',
        'vendor/angular-translate/angular-translate.js',
        'vendor/jquery/charts/easypiechart/jquery.easy-pie-chart.js',
        'vendor/angular-translate-storage-cookie/angular-translate-storage-cookie.js',
        'vendor/angular-cookies/angular-cookies.min.js.map',
        'vendor/angular-translate-storage-local/angular-translate-storage-local.js',
        'vendor/angular-translate-loader-static-files/angular-translate-loader-static-files.js',
        'vendor/jquery/charts/sparkline/jquery.sparkline.min.js',
        'vendor/jquery/charts/flot/jquery.flot.min.js',
        'vendor/jquery/charts/flot/jquery.flot.resize.js',
        'vendor/jquery/charts/flot/jquery.flot.tooltip.min.js',
        'vendor/jquery/charts/flot/jquery.flot.spline.js',
        'vendor/jquery/charts/flot/jquery.flot.orderBars.js',
        'vendor/jquery/charts/flot/jquery.flot.pie.min.js',
        'vendor/screenfull/dist/screenfull.js',


        'vendor/jquery/slimscroll/jquery.slimscroll.min.js',
        'vendor/jquery/sortable/jquery.sortable.js',
        'vendor/jquery/nestable/jquery.nestable.js',
        'vendor/jquery/file/bootstrap-filestyle.min.js',
        'vendor/jquery/slider/bootstrap-slider.js',
        'vendor/jquery/chosen/chosen.jquery.min.js',
        'vendor/jquery/spinner/jquery.bootstrap-touchspin.min.js',
        'vendor/jquery/wysiwyg/bootstrap-wysiwyg.js',
        'vendor/jquery/wysiwyg/jquery.hotkeys.js',
        'vendor/jquery/datatables/jquery.dataTables.min.js',
        'vendor/jquery/datatables/dataTables.bootstrap.js',
        'vendor/jquery/jvectormap/jquery-jvectormap.min.js',
        'vendor/jquery/jvectormap/jquery-jvectormap-world-mill-en.js',
        'vendor/jquery/jvectormap/jquery-jvectormap-us-aea-en.js',
        'vendor/jquery/footable/footable.all.min.js',



        'vendor/ng-grid/ng-grid.min.js',
        'vendor/angular-ui-select/dist/select.min.js',
        'vendor/angular-file-upload/angular-file-upload.min.js',
        'vendor/angular-file-upload/angular-file-upload.min.map',
        'vendor/angular-ui-calendar/src/calendar.js',
        'vendor/ngImgCrop/compile/minified/ng-img-crop.js',
        'vendor/angular-bootstrap-nav-tree/dist/abn_tree_directive.js',
        'vendor/angularjs-toaster/toaster.js',
        'vendor/textAngular/dist/textAngular-sanitize.min.js',
        'vendor/textAngular/dist/textAngular.min.js',
        'vendor/venturocket-angular-slider/build/angular-slider.min.js',
        'vendor/videogular/videogular.min.js',
        'vendor/modules/videogular/plugins/controls.min.js',
        'vendor/videogular-buffering/vg-buffering.min.js',
        'vendor/videogular-overlay-play/vg-overlay-play.min.js',
        'vendor/videogular-poster/vg-poster.min.js',
        'vendor/videogular-ima-ads/vg-ima-ads.min.js',

        //calendar
        'vendor/jquery/jquery-ui-1.10.3.custom.min.js',
        'vendor/jquery/moment.min.js',
        'vendor/jquery/fullcalendar/fullcalendar.min.js',

        //'vendor/ngBracket/ngBracket.min.js',
        'vendor/jquery/challonge-jquery-plugin-master/jquery.challonge.js',
        'vendor/angular-i18n/angular-locale_ru-ru.js'
    ],
    css: [
        'vendor/jquery/nestable/nestable.css',
        'vendor/jquery/slider/slider.css',
        'vendor/jquery/chosen/chosen.css',
        'vendor/jquery/spinner/jquery.bootstrap-touchspin.css',
        'vendor/jquery/datatables/dataTables.bootstrap.css',
        'vendor/jquery/jvectormap/jquery-jvectormap.css',
        'vendor/jquery/footable/footable.core.css',

        'vendor/ng-grid/ng-grid.min.css',
        'vendor/ng-grid/theme.css',
        'vendor/angular-ui-select/dist/select.min.css',
        'vendor/ngImgCrop/compile/minified/ng-img-crop.css',
        'vendor/angular-bootstrap-nav-tree/dist/abn_tree.css',
        'vendor/angularjs-toaster/toaster.css',
        'vendor/venturocket-angular-slider/build/angular-slider.css',

        'vendor/bootstrap/dist/css/bootstrap.css',
        'vendor/bootstrap/dist/css/bootstrap.css.map',
        'vendor/textAngular/src/textAngular.css',
        'vendor/jquery/fullcalendar/fullcalendar.css',
        'vendor/jquery/fullcalendar/theme.css',

        //fONTS
        'vendor/font-awesome/css/font-awesome.min.css',
        'vendor/font-awesome/css/simple-line-icons.css',
        'vendor/font-awesome/css/font.css'
    ],
    assets: [
    ]
  }
};
