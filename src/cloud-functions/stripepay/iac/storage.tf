resource "google_storage_bucket" "stripe-function-bucket" {
  name          = "${var.project_id}-stripe-archive"
  location      = var.region
  storage_class = "STANDARD"

  versioning {
    enabled = true
  }

}