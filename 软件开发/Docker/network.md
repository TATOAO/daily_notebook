

# 网络



docker network ls

docker network inspect network_name

docker network disconnect network_name container_name

docker network create network_name container_name


# 跨应用的网络链接

docker network connect contract_ai_app-network myredis
docker network connect contract_ai_app-network mysql
docker network connect contract_ai_app-network smart-contract
