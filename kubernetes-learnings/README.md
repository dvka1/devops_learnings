# Installing kubectl (Linux example)

```curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" ```

```chmod +x kubectl```

```sudo mv kubectl /usr/local/bin/```

```kubectl version --client
```

# installing kind

```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64```
```chmod +x ./kind```
```sudo mv kind /usr/local/bin/kind
```kind version
```

# Create a Kubernetes cluster using kind

```
Create a Kubernetes cluster using kind 
kubectl get nodes
```

# Build and Load Docker Image into kind

```docker build -t devika/hello:1.0 .
kind load docker-image devika/hello:1.0 --name devika-cluster
```

# Deploy and verify
```
kubectl apply -f hello-deploy.yaml
kubectl get pods
kubectl logs <pod-name>
```

# scale deployment

```
kubectl scale deployment hello-deployment --replicas=5
kubectl get pods

```

# can run as job too 
