data "archive_file" "source" {
  type        = "zip"
  source_dir  = "../src/main"
  output_path = "/tmp/stripe-function.zip"
}

resource "google_storage_bucket_object" "stripe-function-zip" {
  source       = data.archive_file.source.output_path
  content_type = "application/zip"

  name   = "stripe-${data.archive_file.source.output_md5}.zip"
  bucket = google_storage_bucket.stripe-function-bucket.name

  depends_on = [
    google_storage_bucket.stripe-function-bucket,
    data.archive_file.source
  ]

}

resource "google_cloudfunctions_function" "stripe-function" {
  name    = "stripe-event-handler"
  runtime = "python310"

  source_archive_bucket = google_storage_bucket.stripe-function-bucket.name
  source_archive_object = google_storage_bucket_object.stripe-function-zip.name

  entry_point = "process"

  environment_variables = {
    "REDIS_PASSWORD"       = "TheDarkKnight33"
    "STRIPE_API_KEY"       = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
    "GOOGLE_CLOUD_PROJECT" = "${var.project_id}"
    "GOOGLE_EVENTS_TOPIC"  = "${data.terraform_remote_state.pubsub-topics.outputs.google_sheet_event_topic}"
    "PAYMENTS_TOPIC"       = "${data.terraform_remote_state.pubsub-topics.outputs.stripe_payment_event_topic}"
  }

  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = "projects/${var.project_id}/topics/${data.terraform_remote_state.pubsub-topics.outputs.stripe_payment_event_topic}"
  }

  depends_on = [
    google_storage_bucket.stripe-function-bucket,
    google_storage_bucket_object.stripe-function-zip
  ]

}