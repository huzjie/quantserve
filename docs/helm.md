# Helm 部署

```bash
helm install quantserve deploy/helm \
  --set config.mirror=modelscope \
  --set auth.token=YOUR_TOKEN
```
