var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// todo model
var todoSchema = new Schema({
    content: String,
    description:String,
    completed: { type: Boolean, default: false },
    created_at: { type: Date, default: Date.now },
    updated_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Todo', todoSchema);