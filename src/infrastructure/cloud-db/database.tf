resource "google_sql_database" "database" {
  name     = "dk-dev-database-1"
  instance = google_sql_database_instance.db-postgres-instance.name
}