data "archive_file" "source" {
  type        = "zip"
  source_dir  = "../src/main"
  output_path = "/tmp/postgres-function.zip"
}

resource "google_storage_bucket_object" "postgres-function-zip" {
  source       = data.archive_file.source.output_path
  content_type = "application/zip"

  name   = "postgres-${data.archive_file.source.output_md5}.zip"
  bucket = google_storage_bucket.postgres-function-bucket.name

  depends_on = [
    google_storage_bucket.postgres-function-bucket,
    data.archive_file.source
  ]

}

resource "google_cloudfunctions_function" "postgres-function" {
  name    = "postgres-event-handler"
  runtime = "python310"

  source_archive_bucket = google_storage_bucket.postgres-function-bucket.name
  source_archive_object = google_storage_bucket_object.postgres-function-zip.name

  entry_point = "process"

  service_account_email = var.postgres_service_account

  environment_variables = {
    "POSTGRES_USER"         = "${data.terraform_remote_state.dk_dev_db_config.outputs.dk_dev_database_user}"
    "POSTGRES_PASSWORD"     = "${data.terraform_remote_state.dk_dev_db_config.outputs.dk_dev_database_password}"
    "POSTGRES_DB"           = "${data.terraform_remote_state.dk_dev_db_config.outputs.dk_dev_database_name}"
    "POSTGRES_UXPATH"       = "/cloudsql/${data.terraform_remote_state.dk_dev_db_config.outputs.dk_dev_connection_name}"
    "REDIS_PASSWORD"        = "TheDarkKnight33"
    "PYTHONHASHSEED"        = 0
    "GOOGLE_CLOUD_PROJECT"  = "${var.project_id}"
    "GOOGLE_EVENTS_TOPIC"   = "${data.terraform_remote_state.pubsub-topics.outputs.google_sheet_event_topic}"
    "POSTGRES_EVENTS_TOPIC" = "${data.terraform_remote_state.pubsub-topics.outputs.postgres_event_topic}"
  }

  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = "projects/${var.project_id}/topics/${data.terraform_remote_state.pubsub-topics.outputs.postgres_event_topic}"
  }

  depends_on = [
    google_storage_bucket.postgres-function-bucket,
    google_storage_bucket_object.postgres-function-zip
  ]

}