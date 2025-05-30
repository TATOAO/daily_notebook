

# 基础配置

默认需要1800
minikube config set memory 1500

minikube delete
minikube start


```bash
lwt@ubuntu-s-4vcpu-8gb-240gb-intel-sgp1-01:~$ minikube delete
lwt@ubuntu-s-4vcpu-8gb-240gb-intel-sgp1-01:~$ minikube start --cpus=4 --memory=8192
```


# 从配置文件创建depolyment

kubectl apply -f the-config.yaml
kubectl delete -f the-config.yaml

使用文件夹内所有的配置
kubectl apply -f ./a_folder


# 查看
kubectl get nodes
kubectl get pod
kubectl get pod pod_name -o wide

kubectl get services
kubectl get replicaset
kubectl get deployment

kubectl get deployment name -o yaml > yaml_with_status.yaml



# debug
kubectl logs -f [pod name]
-f, --follow=false: Specify if the logs should be streamed.


kubectl exec -it [pod name] -- bin/bash




# CRUD 
kubectl create deployment [name] --image=image [options]


kubectl edit deployment [name]
kubectl delete deployment [name]


# example
kubectl create deployment [name] --image=image
deployment 就是pods的蓝图
kubectl get replicaset 可以看到多少个 replicaset 重复的 pods
pod name = name-replicasetid-podid



kubectl describe pod [pod_name]



# Connection


处理容器间的网络问题:

```bash
kubectl port-forward service/elasticsearch-master 9200:9200
```






