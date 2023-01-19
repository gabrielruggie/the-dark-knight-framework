terraform {

  backend "gcs" {
    bucket = "dark-knight-terraform-state"
    prefix = "dk-pubsub-topics"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("gruggie-service-key.json")

  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_pubsub_topic" "google-sheet-topic" {
  name = "dk.services.sheets"
}

resource "google_pubsub_topic" "postgres-topic" {
  name = "dk.services.postgres"
}

resource "google_pubsub_topic" "stripe-payment-topic" {
  name = "dk.services.payments"
}