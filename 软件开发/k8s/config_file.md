


# 第一层
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: news-monitor-chrome
  labels:
    app: news-monitor
    component: chrome
spec:
   ...
```

## kind

1. Deployment 
2. Service

三个部分:
1. metadata
2. specs
3. status (自动) (etcd)
ps: 如何查看status 
kubectl get deployment name -o yaml > yaml_with_status.yaml


# Spec
Specification


不同的kind 有不同的 Spec


# Connetor

labels: 
selector: 



Service 的 selector 告诉他应该只想哪个 pods 


https://www.youtube.com/watch?v=X48VuDVv0do&ab_channel=TechWorldwithNana
参考这个视频大概1小时:12分的位置
