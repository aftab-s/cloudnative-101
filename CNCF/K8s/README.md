# Minikube example — deploy `aftab2010/coffee-artistry`

This document shows a minimal example to run the `aftab2010/coffee-artistry` static site image on a local Kubernetes cluster using Minikube. It includes two workflows:

- Build & push the Docker image to Docker Hub (the image built from `CNCF/Sample/Dockerfile`).
- Run the image in Minikube (either pulling from Docker Hub, or loading the image into Minikube's Docker daemon so you don't need to push).

This is intentionally simple and meant for local development / testing.

Prerequisites
-------------

- Docker (or Docker Desktop) installed and running
- Minikube installed (https://minikube.sigs.k8s.io/docs/start/)
- kubectl installed and configured (https://kubernetes.io/docs/tasks/tools/)
- (Optional) A Docker Hub account with a repository available for `aftab2010/coffee-artistry`

Paths used in this repo
----------------------

- The Dockerfile used to build the image is at: `CNCF/Sample/Dockerfile` (relative to the repo root). On your machine the path is:

```
D:\Projects\CUSAT-DSC\cloudnative-101\CNCF\Sample\Dockerfile
```

Workflow A — Build and push to Docker Hub (pull from cluster)
-----------------------------------------------------------

1. Build the image locally (run from the `CNCF/Sample` directory):

```powershell
cd D:/Projects/CUSAT-DSC/cloudnative-101/CNCF/Sample
docker build -t aftab2010/coffee-artistry:latest .
```

2. Log in to Docker Hub (use a personal access token for CI; your password works here interactively):

```powershell
docker login
```

3. Push the image to Docker Hub:

```powershell
docker push aftab2010/coffee-artistry:latest
```

4. Start Minikube (if not already running). Use the Docker driver if available:

```powershell
minikube start --driver=docker
```

5. Create Kubernetes resources (Deployment + Service). A `deployment.yaml` is provided in this folder — you can apply it directly:

```powershell
kubectl apply -f CNCF/K8s/deployment.yaml
```

deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: coffee-artistry
spec:
  replicas: 2
  selector:
    matchLabels:
      app: coffee-artistry
  template:
    metadata:
      labels:
        app: coffee-artistry
    spec:
      containers:
        - name: coffee-artistry
          image: aftab2010/coffee-artistry:latest
          ports:
            - containerPort: 80
          livenessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 10
            periodSeconds: 10

---
apiVersion: v1
kind: Service
metadata:
  name: coffee-artistry
spec:
  type: NodePort
  selector:
    app: coffee-artistry
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      # NodePort will be assigned automatically in the 30000-32767 range

```

Apply the manifest:

```powershell
kubectl apply -f deployment.yaml
```

6. Expose the service to your host and open it in a browser. The easiest way with Minikube is:

```powershell
minikube service coffee-artistry --url

# The command prints a URL like http://192.168.49.2:30080 — open that in your browser.
```

Alternatively you can forward a port:

```powershell
# Forward cluster port 80 to local 8080
kubectl port-forward svc/coffee-artistry 8080:80
# Then open http://localhost:8080
```

Workflow B — Use Minikube's Docker daemon (no push required)
---------------------------------------------------------

If you prefer not to push to Docker Hub during development, build the image inside Minikube's Docker daemon and then apply the manifest. Steps (PowerShell):

1. Start minikube (if not already):

```powershell
minikube start --driver=docker
```

2. Point your shell to Minikube's Docker daemon and build there so the image is available to the cluster without a push:

```powershell
# Set environment so `docker build` will use Minikube's Docker daemon
& minikube -p minikube docker-env --shell powershell | Invoke-Expression

cd D:/Projects/CUSAT-DSC/cloudnative-101/CNCF/Sample
docker build -t aftab2010/coffee-artistry:latest .

# (Optional) verify image exists in Minikube's docker
docker images | Select-String coffee-artistry
```

3. Apply the same `deployment.yaml` manifest shown above. Since the image name matches and the image exists in Minikube's daemon, Kubernetes will use the local image.

4. Open the service with:

```powershell
minikube service coffee-artistry --url
```

Notes and troubleshooting
-------------------------

- If you use Workflow A (push to Docker Hub), ensure Minikube nodes can pull the image (network access). Minikube will pull from Docker Hub like any other cluster.
- If the Deployment fails to pull the image and you used Workflow B (built inside Minikube), double-check you have switched the shell to Minikube's Docker daemon before building (step 2). If you restart your PowerShell, re-run the `minikube docker-env` command.
- To inspect resources:

```powershell
kubectl get pods -o wide
kubectl get svc
kubectl logs deployment/coffee-artistry -c coffee-artistry
kubectl describe pod <pod-name>
```

- To stop and delete the demo resources:

```powershell
kubectl delete -f deployment.yaml
minikube stop
minikube delete
```

Security note
-------------

- For CI (GitHub Actions) use a Docker Hub access token stored as a secret (not your account password). The README in `CNCF/Sample` explains `DOCKERHUB_TOKEN` and best practices.

That's it — you should now have a simple, local Kubernetes deployment running `aftab2010/coffee-artistry` on Minikube.

I have added `deployment.yaml` to this folder. I also added a GitHub Actions workflow at `.github/workflows/docker-publish.yml` which builds the image from `CNCF/Sample/Dockerfile` and pushes it to Docker Hub using the `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` repository secrets. You can enable it by adding those secrets in your repository Settings → Secrets.
