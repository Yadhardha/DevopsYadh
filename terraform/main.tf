provider "local" {}
resource "local_file" "devops_project" {
filename = "infra.txt"
content = "Infrastructure"
}
