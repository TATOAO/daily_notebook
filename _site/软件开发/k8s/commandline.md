

# 从配置文件创建depolyment

kubectl apply -f the-config.yaml
kubectl delete -f the-config.yaml

# 查看
kubectl get nodes
kubectl get pod
kubectl get services
kubectl get replicaset
kubectl get deployment


# debug
kubectl logs [pod name]
dubectl exec -it [pod name] -- bin/bash


# CRUD 
kubectl create deployment [name]
kubectl edit deployment [name]
kubectl delete deployment [name]
