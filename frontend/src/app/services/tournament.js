angular.module('djangoTournamentModule', ['djangoRESTResources'])
    .factory('tournamentAttendantsById', ['djResource', function (djResource) {
        return djResource('/api/tournament/attendants/:id/', {id: '@id'}, {
            query: { method:'GET', isArray:true }
        });
    }])
    .factory('tournamentMatches', ['djResource', function (djResource) {
        return djResource('/api/tournament/matches/', {}, {
            query: { method:'GET', params:{}, isArray:true }
        });
    }])
    .factory('tournamentDataById', ['djResource', function (djResource) {
        return djResource('/api/tournament/data/:id/', {id: '@id'}, {
            query: { method:'GET', isArray:false}
        });
    }]);

