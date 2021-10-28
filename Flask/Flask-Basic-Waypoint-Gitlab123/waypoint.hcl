project = "Flask Basic application"

app "flask-basic-app" {
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
          repository = "flask-basic-waypoint-gitlab"
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