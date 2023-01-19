output "dk_dev_connection_name" {
  description = "This is the connection name for the developement database"
  sensitive = true
  value       = google_sql_database_instance.db-postgres-instance.connection_name
}

output "dk_dev_database_user" {
  description = "This is the official admin's user name for the dk development database"
  sensitive = true
  value       = google_sql_user.gabriel-ruggie.name
}

output "dk_dev_database_password" {
  description = "This is the official admin's password for the dk development database"
  sensitive = true
  value       = google_sql_user.gabriel-ruggie.password
}

output "dk_dev_database_name" {
  description = "This is the name of the dk development database"
  value       = google_sql_database.database.name
}