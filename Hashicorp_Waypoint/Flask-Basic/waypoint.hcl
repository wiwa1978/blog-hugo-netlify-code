project = "Flask Todo application"

app "flask_todo_app" {
    build {
        use "docker" {
        }

    }

    deploy {
        use "docker" {
        }
    }
}
