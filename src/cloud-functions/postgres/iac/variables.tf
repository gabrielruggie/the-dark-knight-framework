variable "project_id" {
  description = "The Dark Knight Google CloudProject ID."
  type        = string
}

variable "region" {
  description = "The Dark Knight Google Cloud region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The Dark Knight Google Cloud zone"
  type        = string
  default     = "us-central1-c"
}

variable "postgres_db_username" {
  description = "The Service Account Used By Postgres Event Handler"
  type        = string
}

variable "postgres_db_password" {
  description = "The Service Account Used By Postgres Event Handler"
  type        = string
}

variable "postgres_db_name" {
  description = "The Service Account Used By Postgres Event Handler"
  type        = string
}

variable "postgres_db_uxpath" {
  description = "The Service Account Used By Postgres Event Handler"
  type        = string
}

variable "postgres_service_account" {
  description = "The Service Account Used By Postgres Event Handler"
  type        = string
}