var routerApp = window.angular.module('routerApp', ['ui.router', 'angular-loading-bar']);

routerApp.config(function($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise('/home');

        $stateProvider
        // HOME STATES AND NESTED VIEWS ========================================
        .state('home', {
                url: '/home',
                controller: 'homeController'
            });
    });

routerApp.controller('homeController', function($scope, $http, $location) {

        window.console.log("In home controller...");
        $scope.response_data = {};

        $scope.tocrawl = function() {

            // forming the url    
            var data = {
                url: null,
                depth: null
            };

            var back_url = '/article/?ordering=-up_votes';

            $http.get(back_url, {
                    data: JSON
                }).success(function(data, status, headers, config) {
                    $scope.response_data = data;
                    return;
                })

            .error(function(data, status, headers, config) {
                    window.alert("Error ");
                    return;
                });
        };


        $scope.upvote = function(item) {


            if (item.up_votes == null)
                 item.up_votes = 1;
            else
                item.up_votes = parseInt(item.up_votes)+1;

            var back_url = '/article/'+item.id+'/';

            $http.patch(back_url, item, {
                    data: JSON
                }).success(function(data, status, headers, config) {
                        $scope.tocrawl()
                    return;
                })

            .error(function(data, status, headers, config) {
                    window.alert("Error ");
                    return;
                });
        };

        $scope.tocrawl()

    });