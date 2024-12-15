

# Overview

Azure Key Vault is a cloud service for securely storing and accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, or cryptographic keys. Key Vault service supports two types of containers: 
1. vaults and 
2. managed hardware security module(HSM) pools. 

1. Vaults support storing software and HSM-backed keys, secrets, and certificates. 
2. Managed HSM pools only support HSM-backed keys. See Azure Key Vault REST API overview for complete details.





- Tenant: A tenant is the organization that owns and manages a specific instance of Microsoft cloud services. It's most often used to refer to the set of Azure and Microsoft 365 services for an organization.

- Vault owner: A vault owner can create a key vault and gain full access and control over it. The vault owner can also set up auditing to log who accesses secrets and keys. Administrators can control the key lifecycle. They can roll to a new version of the key, back it up, and do related tasks.

Vault consumer: A vault consumer can perform actions on the assets inside the key vault when the vault owner grants the consumer access. The available actions depend on the permissions granted.

Managed HSM Administrators: Users who are assigned the Administrator role have complete control over a Managed HSM pool. They can create more role assignments to delegate controlled access to other users.

Managed HSM Crypto Officer/User: Built-in roles that are usually assigned to users or service principals that will perform cryptographic operations using keys in Managed HSM. Crypto User can create new keys, but can't delete keys.

Managed HSM Crypto Service Encryption User: Built-in role that is usually assigned to a service accounts managed service identity (for example, Storage account) for encryption of data at rest with customer managed key.

Resource: A resource is a manageable item that's available through Azure. Common examples are virtual machine, storage account, web app, database, and virtual network. There are many more.

Resource group: A resource group is a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. You decide how you want to allocate resources to resource groups, based on what makes the most sense for your organization.

Security principal: An Azure security principal is a security identity that user-created apps, services, and automation tools use to access specific Azure resources. Think of it as a "user identity" (username and password or certificate) with a specific role, and tightly controlled permissions. A security principal should only need to do specific things, unlike a general user identity. It improves security if you grant it only the minimum permission level that it needs to perform its management tasks. A security principal used with an application or service is called a service principal.

Microsoft Entra ID: Microsoft Entra ID is the Active Directory service for a tenant. Each directory has one or more domains. A directory can have many subscriptions associated with it, but only one tenant.

Azure tenant ID: A tenant ID is a unique way to identify a Microsoft Entra instance within an Azure subscription.

Managed identities: Azure Key Vault provides a way to securely store credentials and other keys and secrets, but your code needs to authenticate to Key Vault to retrieve them. Using a managed identity makes solving this problem simpler by giving Azure services an automatically managed identity in Microsoft Entra ID. You can use this identity to authenticate to Key Vault or any service that supports Microsoft Entra authentication, without having any credentials in your code. For more information, see the following image and the overview of managed identities for Azure resources.
