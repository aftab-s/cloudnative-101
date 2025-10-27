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

- A GitHub Actions workflow was added at `.github/workflows/docker-publish.yml`. It builds the image from `CNCF/Sample` and pushes to Docker Hub using repository secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`.
- Note: `DOCKERHUB_TOKEN` should be a Docker Hub personal access token (recommended) rather than your account password. See `CNCF/Sample/README.md` for details.
 - Public Docker Hub repository for this demo: https://hub.docker.com/repository/docker/aftab2010/coffee-artistry/
	 You can pull the published image directly with `docker pull aftab2010/coffee-artistry:latest`.

Kubernetes (Minikube) example
----------------------------

- A minimal Kubernetes manifest is provided at `CNCF/K8s/deployment.yaml` (Deployment + NodePort Service) which runs the image `aftab2010/coffee-artistry:latest`.
- Full Minikube instructions are in `CNCF/K8s/README.md` (it shows two workflows: push to Docker Hub and pull from cluster, or build inside Minikube's Docker daemon so you don't need to push).

To deploy locally with Minikube (example):

```powershell
minikube start --driver=docker
kubectl apply -f CNCF/K8s/deployment.yaml
minikube service coffee-artistry --url
```

Notes & next steps
------------------

- The sample site's CSS was updated to be responsive; a mobile-friendly layout and hero fixes were applied.
- For production-grade Kubernetes manifests, consider adding `resources.requests`/`limits`, readiness probes, and an Ingress resource.
- If you want, I can:
	- Add resource requests/limits to `CNCF/K8s/deployment.yaml` (small sensible defaults),
	- Add an Ingress manifest and instructions to enable Minikube ingress, or
	- Fully scaffold a React + Tailwind redesign in `CNCF/Sample` (we discussed this earlier).

Security
--------

- Do not commit secrets to the repository. Store CI secrets (Docker Hub tokens, cloud credentials) in your GitHub repository Settings → Secrets.

Where to look next
------------------

- `CNCF/Sample/README.md` — build/run/push sample site
- `CNCF/K8s/README.md` — Minikube deployment instructions
- Other folders (`EC2/`, `S3/`, `Lambda/`) contain their respective guides

If you'd like I can also run Minikube here and validate the deployment (note: the current environment may not allow running Minikube). If you'd prefer, I can add the extra manifests you requested (Ingress, resources) — tell me which option you prefer.