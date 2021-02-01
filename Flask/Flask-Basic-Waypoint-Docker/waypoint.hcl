project = "Flask Todo application"

app "flask_todo_app" {
    labels = {
    "service" = "flask-todo",
    "env"     = "dev"
  }
    build {
        use "docker" {
        }

    }

    deploy {
        use "docker" {
            service_port = 8081
        }
    }
}