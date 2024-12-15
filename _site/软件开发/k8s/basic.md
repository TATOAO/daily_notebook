


# What does Kubernetes does
helps you manage containerized applications in different deplyment environments



# conponents

- Pod = container

each pods has its own ip address


ephemeral  = easy to die = born with new ip address


- Services  permanent IP  address
- Ingress（入口资源）

## Ingress & Service

作用
HTTP/HTTPS 路由：根据请求的主机名和 URL 路径，将流量转发到相应的 Service。

虚拟主机：支持基于主机名的虚拟主机配置，使多个服务共享同一个 IP 地址和端口。

TLS/SSL 支持：可以在 Ingress 中配置 TLS 证书，实现 HTTPS 加密。

负载均衡：在 HTTP/HTTPS 层面上实现流量的负载均衡。


### Ingress Controller
Ingress 资源本身只定义了路由规则，需要一个 Ingress Controller 来实际执行这些规则。Ingress Controller 是部署在集群中的特殊 Pod，常见的有：

NGINX Ingress Controller

Traefik

HAProxy

Istio Ingress Gateway

### 工作原理
创建 Ingress 资源：用户定义 Ingress 规则，描述如何将外部请求路由到内部服务。

Ingress Controller 监听：Ingress Controller 监听集群中的 Ingress 资源变化。

更新路由配置：根据 Ingress 规则，Ingress Controller 更新其内部的路由配置（如 NGINX 配置）。

处理请求：当外部请求到达 Ingress Controller 时，它根据规则将请求转发到相应的 Service。




### Service 和 Ingress 的关系
互补关系：Service 和 Ingress 是相互协作的。Service 提供了 Pod 的稳定访问入口，而 Ingress 则定义了外部请求如何通过 HTTP/HTTPS 协议访问这些 Service。

不同的关注点：

Service：关注集群内部的服务发现和负载均衡，主要解决 Pod 的不稳定性和动态性。

Ingress：关注集群外部的 HTTP/HTTPS 请求如何路由到内部的 Service，实现基于域名和路径的访问控制。

组合使用：通常情况下，Ingress 会引用一个或多个 Service，将外部请求按照规则转发到相应的 Service，然后由 Service 分发到后端的 Pod。



## config map & secrect


## Volumns
硬盘 


## Deplyments - abstraction of Pods (like Dockerfile?)



Deployment for stateless applications
StatefulSet for statful applications



# Master and nodes


node - worker 
must have 3 process:
1. container runtime (docker)
2. kubelet (interacts with both contaner and node) (starts the pod with a contaner inside)
3. kube proxy (forward the request)


master: 
1. schedule pod
2. monitor
3. re-schedule /restart pod
4. join a new node

must have 4 process:
1. api server - cluster gateway  - autho
2. scheduler - decide where to put the pod
3. controller manager - detects 
4. etcd , key  value store, - cluster info

# minikube cluster
all in one machine for test and debug and develop


# kuberctl




