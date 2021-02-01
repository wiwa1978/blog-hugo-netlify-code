project = "Flask ECR ECS"

app "flask_ecr_ecs" {
    labels = {
        "service" = "flask-todo",
        "env"     = "dev"
    }
    build {
        use "pack" {}
        registry {
        use "aws-ecr" {
            region = "us-east-1"
            repository = "waypoint-example"
            tag = "latest"
        }
        }
    }

    deploy {
        use "aws-ecs" {
            region = "us-east-1"
            memory = "512"
        }
    }
}