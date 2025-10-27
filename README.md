# Cloud Native & AWS Practice Guide

This repository is a collection of small, focused examples and guides for learning cloud-native and AWS topics. It contains multiple demo folders (static sites, container examples, and deployment recipes) with step-by-step instructions so you can run them locally and on a small Kubernetes cluster.

Top-level contents
------------------

- `EC2/` — examples and notes for EC2 (SSH, basic server setup).
- `S3/` — S3 usage examples and CLI snippets.
- `Lambda/` — small Lambda demo and test event.
- `CNCF/` — Cloud-native examples (static sample site, Dockerfile, Kubernetes manifests, and CI workflow). See below for details.

Quick start — sample static site
--------------------------------

We included a small static site (designed from a Figma mockup) under `CNCF/Sample/` that demonstrates containerizing a static site with Docker and deploying it to Kubernetes.

- Files of interest:
	- `CNCF/Sample/index.html`, `CNCF/Sample/style.css`, `CNCF/Sample/assets/` — the static site
	- `CNCF/Sample/Dockerfile` — builds an Nginx image that serves the site
	- `CNCF/Sample/README.md` — instructions to build/run locally and how to push to Docker Hub

Serve locally without Docker
1. Open a terminal and run (from `CNCF/Sample`):

```powershell
cd D:/Projects/CUSAT-DSC/cloudnative-101/CNCF/Sample
python -m http.server 8000
# then open http://localhost:8000
```

Build and run with Docker
1. Build the image:

```powershell
cd D:/Projects/CUSAT-DSC/cloudnative-101/CNCF/Sample
docker build -t aftab2010/coffee-artistry:latest .
```

2. Run the container:

```powershell
docker run -d --name coffee-artistry -p 8080:80 aftab2010/coffee-artistry:latest
# then open http://localhost:8080
```

CI / Docker Hub
----------------

- A GitHub Actions workflow is included at `.github/workflows/docker-publish.yml`. It uses Docker buildx with layer caching to build the image from `CNCF/Sample` and push to Docker Hub.
- The workflow pushes both `:latest` and `:${{ github.sha }}` tags for traceability.
- Requires repository secrets: `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` (use a Docker Hub personal access token, not your password).
- Public Docker Hub repository: https://hub.docker.com/repository/docker/aftab2010/coffee-artistry/
  
  Pull the published image directly: `docker pull aftab2010/coffee-artistry:latest`
 
Kubernetes (Minikube) example
----------------------------

- A minimal Kubernetes manifest is provided at `CNCF/K8s/deployment.yaml` (Deployment + NodePort Service) which runs the image `aftab2010/coffee-artistry:latest`.
- Full Minikube instructions are in `CNCF/K8s/README.md` (it shows two workflows: push to Docker Hub and pull from cluster, or build inside Minikube's Docker daemon so you don't need to push). 

To deploy locally with Minikube (example):

```powershell
minikube start --driver=docker
kubectl apply -f CNCF/K8s/deployment.yaml
minikube service coffee-svc -n coffee-artistry --url
```

**Important**: The manifest creates resources in the `coffee-artistry` namespace. The Deployment is `coffee-container` and the Service is `coffee-svc`. Always use `-n coffee-artistry` with kubectl and minikube commands when working with this deployment.

Notes & next steps
------------------

- The sample site's CSS was updated to be responsive with mobile-friendly layouts and hero section fixes.
- The Kubernetes manifest includes resource requests/limits (cpu: 100m/250m, memory: 128Mi/256Mi) and liveness probes.
- Resources are deployed in the `coffee-artistry` namespace (remember to use `-n coffee-artistry` with kubectl commands). The Deployment created is named `coffee-container` and the Service `coffee-svc`.
- The GitHub Actions workflow uses Docker buildx with build caching and pushes multiple tags (`:latest` and `:sha`).

Security
--------

- Do not commit secrets to the repository. Store CI secrets (Docker Hub tokens, cloud credentials) in your GitHub repository Settings → Secrets.

Where to look next
------------------

- `CNCF/Sample/README.md` — build/run/push sample site and Docker Hub details
- `CNCF/K8s/README.md` — Minikube deployment instructions with namespace guidance
- `.github/workflows/docker-publish.yml` — CI workflow for automated builds
- Other folders (`EC2/`, `S3/`, `Lambda/`) contain their respective AWS service guides

---

**Quick verification checklist:**
1. ✅ Static site works locally (python http.server or Docker)
2. ✅ Docker image builds and pushes to Docker Hub
3. ✅ Kubernetes deployment runs in Minikube (use `-n coffee-artistry` flag; Deployment: `coffee-container`, Service: `coffee-svc`)
4. ✅ GitHub Actions workflow configured with secrets