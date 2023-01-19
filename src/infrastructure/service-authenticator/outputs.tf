output "service_url" {
  description = "This is the public url to access the ASTACK authentication microservice"
  value       = google_cloud_run_service.astack-authenticator.status[0].url
}