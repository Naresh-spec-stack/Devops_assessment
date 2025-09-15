# Senior DevOps Take-Home Test

## Overview
This project implements a **Database Anti-Corruption Layer REST API** using **Flask + PostgreSQL**, deployed on Kubernetes with a **GitOps-style workflow**.

Developers can self-service changes by editing the `api/config.yaml` file (Config-as-Code), which maps REST endpoints to SQL queries and DB column → JSON response fields.

## Features
- **Kubernetes** deployments for PostgreSQL, API, and local Docker registry.
- **Config-as-Code** (`api/config.yaml`) for API endpoint → SQL mappings.
- **GitOps / CI/CD**: Changes to `main` branch rebuild images and redeploy automatically.
- **Local cluster setup** with `kind`.

## File Structure
## api/ # Python Flask API
## db/ # Database init SQL
## k8s/ # Kubernetes manifests
## scripts/ # Helper scripts
## .github/ # CI/CD workflow

## Setup Instructions

### 1. Start Local K8s Cluster

## ./scripts/kind-setup.sh

### 2.Deploy Components

## kubectl apply -f k8s/

### 3.Build & Push API Image

## ./scripts/push-image.sh

### 4.Access the APIS

## kubectl port-forward svc/api-service -n devops-test 3000:3000
## curl http://localhost:3000/users
## curl http://localhost:3000/products


