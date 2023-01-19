terraform {

  backend "gcs" {
    bucket = "dark-knight-terraform-state"
    prefix = "dk-astack-containers"
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