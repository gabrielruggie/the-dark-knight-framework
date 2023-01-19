output "google_sheet_event_topic" {
  description = "This is the event topic for the google sheet scraper service"
  value       = google_pubsub_topic.google-sheet-topic.name
}

output "postgres_event_topic" {
  description = "This is the event topic for the postgres service"
  value       = google_pubsub_topic.postgres-topic.name
}

output "stripe_payment_event_topic" {
  description = "This is the event topic for the stripe payment service"
  value       = google_pubsub_topic.stripe-payment-topic.name
}