This is basic rundown of how this CI/CD pipeline is setup on azure using github actions 

Azure account with 100$ student credit

1. Authenticating azure cli using microsoft account
```
az login
```

2. Creating resource group specifically for BookXchange in southindia (nearest datacenter with lowest latency from Nepal)
```
az group create --name "BookXchange" --location southindia
```

3. Creating AZURE_CREDENTIALS for github actions authentication with azure services.Store the json output into AZURE_CREDENTIALS variable in github repo> settings > secrets(subscription id taken from above command output)
```
az ad sp create-for-rbac --name BookXchange --role contributor --scopes /subscriptions/{subscription_id}/resourceGroups/BookXchange --sdk-auth
```

4. Creating separate registry for development environment, and getting DEV_REGISTRY_LOGIN_SERVER, DEV_REGISTRY_USERNAME, DEV_REGISTRY_PASSWORD,  RESOURCE_GROUP(ClientId from above output)
```
az acr create --resource-group BookXchange --name bookxchangedevelopment --sku Basic --location southindia
$registryId=$(az acr show \
  --name bookxchangedevelopment \
  --resource-group BookXchange \
  --query id --output tsv)
az role assignment create \
  --assignee {ClientId} \
  --scope $registryId \
  --role AcrPush
```


5. Creating postgres server and database for development server
```
az postgres flexible-server create --admin-user {postgres username} \\
    --admin-password {postgres password} --database-name bookxchangedatabasedevelopment \\
    --location southindia --password-auth Enabled --resource-group BookXchange \\
    --sku-name Standard_B1ms --storage-size 32 --version 14 --tier Burstable
```

6. Creating azure kubernetes cluster
```
az aks create --name bookxchange-kluster-development --resource-group BookXchange \\
    --node-count 2 --location southindia --generate-ssh-keys --ip-families ipv4,ipv6
```

7. Downloading cluster credentials (optional)
```
az aks get-credentials --name bookxchange-kluster-development --resource-group BookXchange
```

