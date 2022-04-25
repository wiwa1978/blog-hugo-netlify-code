variable "api_key" {
  description = "API Key DigitalOcean"
  default     = env("DO_API_KEY")
}