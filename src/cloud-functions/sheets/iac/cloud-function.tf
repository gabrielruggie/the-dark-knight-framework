data "archive_file" "source" {
  type        = "zip"
  source_dir  = "../src/main"
  output_path = "/tmp/google-sheets-function.zip"
}

resource "google_storage_bucket_object" "sheet-function-zip" {
  source       = data.archive_file.source.output_path
  content_type = "application/zip"

  name   = "sheets-${data.archive_file.source.output_md5}.zip"
  bucket = google_storage_bucket.google-sheets-function-bucket.name

  depends_on = [
    google_storage_bucket.google-sheets-function-bucket,
    data.archive_file.source
  ]

}

resource "google_cloudfunctions_function" "google-sheet-function" {
  name    = "sheets-event-handler"
  runtime = "python310"

  source_archive_bucket = google_storage_bucket.google-sheets-function-bucket.name
  source_archive_object = google_storage_bucket_object.sheet-function-zip.name

  entry_point = "process"

  environment_variables = {
    "REDIS_PASSWORD"        = "TheDarkKnight33"
    "TEST_YMBL_PRICE"       = 100
    "GOOGLE_CLOUD_PROJECT"  = "${var.project_id}"
    "GOOGLE_EVENTS_TOPIC"   = "${data.terraform_remote_state.pubsub-topics.outputs.google_sheet_event_topic}"
    "POSTGRES_EVENTS_TOPIC" = "${data.terraform_remote_state.pubsub-topics.outputs.postgres_event_topic}"
    "PAYMENTS_TOPIC"        = "${data.terraform_remote_state.pubsub-topics.outputs.stripe_payment_event_topic}"
  }

  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = "projects/${var.project_id}/topics/${data.terraform_remote_state.pubsub-topics.outputs.google_sheet_event_topic}"
  }

  depends_on = [
    google_storage_bucket.google-sheets-function-bucket,
    google_storage_bucket_object.sheet-function-zip
  ]

}