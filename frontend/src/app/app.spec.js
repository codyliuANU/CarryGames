describe( 'AppCtrl', function() {
  describe( 'isCurrentUrl', function() {
    var AppCtrl,
        location,
        scope;

    beforeEach( module( 'app' ) );

    beforeEach( inject( function( $controller, $location, $rootScope ) {
      location = $location;
      scope = $rootScope.$new();
      AppCtrl = $controller( 'AppCtrl', { $location: location, $scope: scope });
    }));

    it( 'should pass a dummy test', inject( function() {
      expect( AppCtrl ).toBeTruthy();
    }));
  });
});
