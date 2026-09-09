# Deployment Guide

## Docker Compose
For single-node deployments:
```bash
docker-compose up -d
```

## Kubernetes
Helm charts are available in the `charts/` directory.
```bash
helm install infraops ./charts/infraops -n infraops --create-namespace
```
