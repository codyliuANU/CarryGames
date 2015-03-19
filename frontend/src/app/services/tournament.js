angular.module('djangoTournamentModule', ['djangoRESTResources'])
    .factory('tournamentAttendants', ['djResource', function (djResource) {
        return djResource('/api/tournament/attendants/', {}, {
            query: { method:'GET', params:{}, isArray:true }
        });
    }])
    .factory('tournamentMatches', ['djResource', function (djResource) {
        return djResource('/api/tournament/matches/', {}, {
            query: { method:'GET', params:{}, isArray:true }
        });
    }]);

