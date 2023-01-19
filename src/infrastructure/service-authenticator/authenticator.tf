resource "google_cloud_run_service" "astack-authenticator" {
  name     = "astack-authenticator"
  location = var.region

  template {
    spec {
      
      containers {
        image = var.service-image-url

        env {
          name  = "API_VERSION"
          value = "beta-v1.0"
        }
        env {
          name  = "POSTGRES_USER"
          value = "dk-admin-gruggie"
        }
        env {
          name  = "POSTGRES_PASSWORD"
          value = "TheDarkKnight33"
        }
        env {
          name  = "POSTGRES_DB"
          value = "test-dk-database-1"
        }
        env {
          name  = "POSTGRES_HOST"
          value = "database"
        }
        env {
          name  = "TOKEN_EXPIRE_TIME_MINUTES"
          value = 60
        }
        env {
          name  = "TOKEN_SECRET_KEY"
          value = "dktokentestkey"
        }
        env {
          name  = "TOKEN_ALGORITM"
          value = "HS256"
        }
        env {
          name  = "REDIS_PASSWORD"
          value = "TheDarkKnight33"
        }
        env {
          name  = "DK_VALIDATION_KEY"
          value = "dk-validation-key"
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }



}

resource "google_cloud_run_service_iam_member" "public_users" {
  service  = google_cloud_run_service.astack-authenticator.name
  location = var.region
  role     = "roles/run.invoker"
  member   = "allUsers"
}