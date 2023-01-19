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

variable "instance_password" {
  description = "The Dark Knight Google Cloud zone"
  type        = string
}

variable "db_password" {
  description = "The Dark Knight Google Cloud zone"
  type        = string
}