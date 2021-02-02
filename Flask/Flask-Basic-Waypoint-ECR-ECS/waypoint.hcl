project = "Flask Basic application with ECR and ECS"

app "flask-ecs" {
    labels = {
      "service" = "flask-basic",
      "env"     = "dev"
    }

    build {
      use "pack" {
        builder     = "heroku/buildpacks:develop"
        disable_entrypoint = false
      }
      registry {
        use "aws-ecr" {
          region = "eu-central-1"
          repository = "flask-basic-waypoint-ecs"
          tag = "latest"
        }
      }
    }

    deploy {
      use "aws-ecs" {
        region = "eu-central-1"
        memory = "512"
      }
    }
}