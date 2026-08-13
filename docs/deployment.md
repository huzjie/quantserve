# 部署指南

## Docker

```bash
docker build -t quantserve .
docker run -p 8000:8000 quantserve
```

## docker-compose

```bash
docker compose up -d
```

## Kubernetes

```bash
kubectl apply -k deploy/k8s
```

## Helm

```bash
helm install quantserve deploy/helm
```
