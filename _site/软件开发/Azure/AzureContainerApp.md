

# Use Case
This reference implementation uses Container Apps features in the following ways:

1. HTTPS Ingress: Used to expose the Ingestion service to the internet.
2. Internal Service Discovery: Ensures internal services (Delivery, DroneScheduler, and Package) can be reached by the Workflow service.
3. Managed Identities: User-assigned managed identities authenticate with Azure KeyVault from Delivery and DroneScheduler services.
4. Secrets Management: Secure management of secrets for Package, Ingestion, and Workflow services.
5. Container Registry: Fabrikam Drone Delivery leverages Azure Container Registry (ACR) for publishing Docker images.
6. Revisions: Azure Container Apps' revision feature is used for safe updates. The Workflow Service, operating as a message consumer, deploys in single revision mode.
7. Azure Resource Manager Templates: The application is deployed using Azure Resource Manager templates, simplifying deployment.
8. Log Analytics: Container logs are reviewed in Log Analytics without the need for additional configuration.


# container config json

```json

{
  "properties": {
    "template": {
      "containers": [
        {
          "name": "main",
          "image": "[parameters('container_image')]",
          "env": [
            {
              "name": "HTTP_PORT",
              "value": "80"
            },
            {
              "name": "SECRET_VAL",
              "secretRef": "mysecret"
            }
          ],
          "resources": {
            "cpu": 0.5,
            "memory": "1Gi"
          },
          "volumeMounts": [
            {
              "mountPath": "/appsettings",
              "volumeName": "appsettings-volume"
            }
          ],
          "probes": [
            {
              "type": "liveness",
              "httpGet": {
                "path": "/health",
                "port": 8080,
                "httpHeaders": [
                  {
                    "name": "Custom-Header",
                    "value": "liveness probe"
                  }
                ]
              },
              "initialDelaySeconds": 7,
              "periodSeconds": 3
            },
            {
              "type": "readiness",
              "tcpSocket": {
                "port": 8081
              },
              "initialDelaySeconds": 10,
              "periodSeconds": 3
            },
            {
              "type": "startup",
              "httpGet": {
                "path": "/startup",
                "port": 8080,
                "httpHeaders": [
                  {
                    "name": "Custom-Header",
                    "value": "startup probe"
                  }
                ]
              },
              "initialDelaySeconds": 3,
              "periodSeconds": 3
            }
          ]
        }
      ]
    },
    "initContainers": [
      {
        "name": "init",
        "image": "[parameters('init_container_image')]",
        "resources": {
          "cpu": 0.25,
          "memory": "0.5Gi"
        },
        "volumeMounts": [
          {
            "mountPath": "/appsettings",
            "volumeName": "appsettings-volume"
          }
        ]
      }
    ]
    ...
  }
  ...
}

```


# Multiple containers

In advanced scenarios, you can run multiple containers in a single container app. Use this pattern only in specific instances where your containers are tightly coupled.

For most microservice scenarios, the best practice is to deploy each service as a separate container app.

The multiple containers in the same container app share hard disk and network resources and experience the same application lifecycle.

There are two ways to run multiple containers in a container app: sidecar containers and init containers.
