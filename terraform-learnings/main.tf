terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

# Create a namespace
resource "kubernetes_namespace" "demo" {
  metadata {
    name = "demo"
  }
}

# Create a simple Nginx pod
resource "kubernetes_pod" "nginx" {
  metadata {
    name      = "nginx-pod"
    namespace = kubernetes_namespace.demo.metadata[0].name
  }

  spec {
    container {
      name  = "nginx"
      image = "nginx:latest"
      port {
        container_port = 80
      }
    }
  }
}

