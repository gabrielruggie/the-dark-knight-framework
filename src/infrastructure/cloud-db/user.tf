resource "google_sql_user" "gabriel-ruggie" {
  name     = "dk-admin-gruggie"
  project  = var.project_id
  instance = google_sql_database_instance.db-postgres-instance.name
  password = var.db_password
}