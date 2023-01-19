resource "google_sql_database_instance" "db-postgres-instance" {
  name             = "dk-dev-instance"
  project          = var.project_id
  database_version = "POSTGRES_14"
  region           = var.region

  settings {
    tier              = "db-f1-micro"
    disk_size         = 10
    availability_type = "ZONAL"
  }
}