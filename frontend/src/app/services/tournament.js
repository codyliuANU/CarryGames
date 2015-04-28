angular.module('djangoTournamentModule', ['djangoRESTResources'])
    .factory('tournamentAttendantsById', ['djResource', function (djResource) {
        return djResource('/api-v1/attendants/:id/', {id: '@id'}, {
            query: { method:'GET', isArray:true }
        });
    }])
    .factory('tournamentMatches', ['djResource', function (djResource) {
        return djResource('/api-v1/matches/:id/', {id: '@id'}, {
            query: { method:'GET', params:{}, isArray:true }
        });
    }])
    .factory('tournamentById', ['djResource', function (djResource) {
        return djResource('/api-v1/tournaments/:id/', {id: '@id'}, {
            query: { method:'GET', params:{} }
        });
    }])
    .factory('tournaments', ['djResource', function (djResource) {
        return djResource('/api-v1/tournaments/', {}, {
            query: { method:'GET', params:{}, isArray:true },
            save: { method: 'POST'}
        });
    }])
    .factory('tournamentDataById', ['djResource', function (djResource) {
        return djResource('/api-v1/data/:id/', {id: '@id'}, {
            query: { method:'GET', isArray:false}
        });
    }])
    .factory('attendants', ['djResource', function (djResource) {
        return djResource('/api-v1/attendants/', {}, {
            save: { method: 'POST'}
        });
    }])
    .factory('attendantsByTournamentId', ['djResource', function (djResource) {
        return djResource('/api-v1/attendants/:id/', {id: '@id'}, {
            query: { method:'GET', isArray:true}
        });
    }])
;

