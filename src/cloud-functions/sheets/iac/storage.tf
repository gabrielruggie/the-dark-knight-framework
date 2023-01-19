resource "google_storage_bucket" "google-sheets-function-bucket" {
  name          = "${var.project_id}-sheets-archive"
  location      = var.region
  storage_class = "STANDARD"

  versioning {
    enabled = true
  }

}