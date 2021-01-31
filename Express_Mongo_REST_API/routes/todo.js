var express = require('express');
var router = express.Router();
var Todo = require('../models/todo');

// GET New Todo page
router.get('/new', function(req, res) {
	console.log("Show page to create new todo item");
    res.render('todos/new', { title: 'Add New Todo' });
});

// route middleware to validate :id
router.param('id', function(req, res, next, id) {
    Todo.findById(id, function (err, todo) {
        //if it isn't found, we are going to repond with 404
        if (err) {
            console.log("Todo item with " + id + " was not found in the database");
            res.status(404)
            var err = new Error('Not Found');
            err.status = 404;
            res.format({
                html: function(){
                    next(err);
                },
                json: function(){
                    res.json({message : err.status  + " " + err});
                }
            });
        //if it is found we continue on
        } else {
            console.log(todo);
            req.id = id;
            next(); 
        } 
    });
});

// -----------------------------------------------------------------------------------------
// Matches routes without identifiers

router.route('/')
    //GET all todos
    .get(function(req, res, next) {
        Todo.find({}, function (err, todos) {
              if (err) {
                  return console.error(err);
              } else {
              		console.log("Showing all todo items");
              		res.format({
                    html: function(){
                        res.render('todos/index', {
                            title: 'All my todos', 
                            "todos" : todos
                        });
                    },
                    json: function(){
                        res.json(todos);
                    }
                });
              }     
        });
    })

	//POST a new todo item
    .post(function(req, res) {
		var content = req.body.content;
        var completed = false;
        var description = req.body.description;


        Todo.create({
            content : content,
            completed : completed,
            description : description,
           
        }, function (err, todo) {
            if (err) {
            	res.send("Todo item was not created succesfully");
                console.log("Todo item was not created succesfully");
            } 
            else {
                console.log('Created new todo item: ' + todo);
                res.format({
					html: function(){
                        res.location("todos");
                        res.redirect("/todos");
                    },
                    json: function(){
                        res.json(todo);
                    }
                });
              }
        })
    });



// -----------------------------------------------------------------------------------------
// Matches routes with identifiers

/* SHOW single todo item */
router.route('/:id/show')
	.get(function(req, res) {
    	Todo.findById(req.id, function (err, todo) {
	      	if (err) {
	        	console.log('Todo item with id ' + todo._id + ' could not be found ' + err);
	        	res.send('Todo item with id ' + todo._id + ' could not be found ' + err);
	      	} 
	      	else {
	        	console.log('Show todo item with id ' + todo._id);
	        	res.format({
		        	html: function(){
		             	res.render('todos/show', {
		                	"todo" : todo
		              	});
		          	},
		          	json: function(){
		              	res.json(todo);
		          	}
	        	});
	      	}
    	});
  	});

/* EDIT single todo item */
router.route('/:id/')
	//GET single todo item
	.get(function(req, res) {
	    Todo.findById(req.id, function (err, todo) {
	        if (err) {
	            console.log('Todo item could not be found ' + err);
	        } 
	        else {
	        	console.log('Edit todo item with id ' + todo._id);
              	res.format({
	                html: function(){
	                    res.render('todos/edit', {
	                        title: 'Todo' + todo._id,
                            "todo" : todo
	                    });
	                },
	                json: function(){
	                    res.json(todo);
	                }
	            });
	        }
	    });
	})

	//PUT to update todo item
	.put(function(req, res) {
	    var content = req.body.content;
	    var description = req.body.description;
	    var completed = req.body.completed;
	    var updated_at = new Date();
	    console.log("New time is " + updated_at);
	   
	    Todo.findById(req.id, function (err, todo) {
	        todo.update({
	            content : content,
	            description : description,
	            completed : completed,
	            updated_at : updated_at,
	           
	        }, function (err, todoID) {
	        	if (err) {
	        		console.log('Todo item could not be found ' + err);
	            	res.send('Todo item could not be found ' + err);
	          	} 
	          	else {
	          		console.log('Updated todo item with id ' + todo._id);
	                res.format({
	                    html: function(){
	                        res.redirect("/todos");
	                    },
	                    //JSON responds showing the updated values
	                    json: function(){
	                        res.json(todo);
	                    }
	                });
	           	}
	        })
	    });
	})

	//DELETE a todo item
	.delete(function (req, res){
	    Todo.findById(req.id, function (err, todo) {
	        if (err) {
	            console.log('Todo item could not be found ' + err);
	            res.send('Todo item could not be found ' + err);
	        } 
	        else {
	            todo.remove(function (err, todo) {
	                if (err) {
	                    console.log('Todo item could not be deleted ' + err);
	            		res.send('Todo item could not be deleted ' + err);
	                } 
	                else {
	                    console.log('Deleted todo item with id ' + todo._id);
	                    res.format({
	                        html: function(){
	                            res.redirect("/todos");
	                        },
	                        //JSON returns the item with the message that is has been deleted
	                        json: function(){
	                            res.json({message : 'deleted',
	                                item : todo
	                            });
	                        }
	                    });
	                }
	            });
	        }
	    });
	});


module.exports = router;