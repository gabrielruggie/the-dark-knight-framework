resource "google_storage_bucket" "postgres-function-bucket" {
  name          = "${var.project_id}-postgres-archive"
  location      = var.region
  storage_class = "STANDARD"

  versioning {
    enabled = true
  }

}