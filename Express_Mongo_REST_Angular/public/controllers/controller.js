
var myApp = angular.module('myApp', []);
myApp.controller('AppCtrl', ['$scope', '$http', function($scope, $http) {
   
url = 'http://localhost:3000/todos/'

var refresh = function() {
  $http.get(url).success(function(response) {
    $scope.todolist = response;
    $scope.todo = "";
    $scope.todo.edit = false;
  });
};

refresh();

$scope.addTodo = function() {
  console.log($scope.todo);
  $http.post(url, $scope.todo).success(function(response) {
    console.log(response);
    refresh();
  });
};

$scope.removeTodo = function(id) {
  $http.delete(url + id).success(function(response) {
    console.log("deleting: " + response);
    refresh();
  });
};

$scope.editTodo = function(id) {
  console.log(id);
  $http.get(url + id).success(function(response) {
    $scope.todo = response;
    $scope.todo.edit = true;
  });

};

$scope.updateTodo = function() {
  console.log("Completed" + $scope.todo.completed);
  $http.put(url + $scope.todo._id, $scope.todo).success(function(response) {
     console.log("new updated: " + response.updated_at);
    refresh();
 	})
};

}]);