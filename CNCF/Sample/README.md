# Coffee-Artistry

A basic static HTML/CSS sample website (designed from a Figma mockup) used to demonstrate containerization with Docker.

This README shows how to build a Docker image from the included `Dockerfile`, run the site locally in a container, and push the image to Docker Hub.

## What this repository contains

- `index.html`, `style.css`, and the `assets/` folder — the static site
- `Dockerfile` — builds an Nginx-based image that serves the static site on port 80

## Prerequisites

- Docker installed and running (Docker Desktop, Docker Engine, etc.)
- A Docker Hub account and your Docker Hub username (we'll call it `<DOCKERHUB_USERNAME>` in examples)

## Quick contract

- Input: this repository (root contains `Dockerfile`, `index.html`, `style.css`, `assets/`).
- Output: a Docker image that serves the static site and can be pushed to Docker Hub.
- Success: you can access the site at http://localhost:8080 after running the provided commands.

Edge cases covered: missing Docker, Docker daemon not running, incorrect Docker Hub credentials.

## How the `Dockerfile` works (short)

The included `Dockerfile` uses the official `nginx:alpine` image, copies the static files into Nginx's `/usr/share/nginx/html` directory, exposes port 80, and starts Nginx. The container serves the site at container port 80.

## Build the Docker image

Replace `<DOCKERHUB_USERNAME>` with your Docker Hub username. Run this in the repository root (where `Dockerfile` is located).

```powershell
docker build -t <DOCKERHUB_USERNAME>/coffee-artistry:latest .
```

This produces an image named `<DOCKERHUB_USERNAME>/coffee-artistry:latest`.

## Run the site locally

Run the container and map container port 80 to host port 8080 so you can open it in a browser:

```powershell
docker run -d --name coffee-artistry -p 8080:80 <DOCKERHUB_USERNAME>/coffee-artistry:latest

# then open http://localhost:8080 in your browser
```

To see logs or verify the container:

```powershell
docker ps
docker logs coffee-artistry
```

To stop and remove the container:

```powershell
docker stop coffee-artistry; docker rm coffee-artistry
```

## Tagging and pushing to Docker Hub

1. Login to Docker Hub from your terminal (PowerShell):

```powershell
docker login
```

2. (Optional) Tag the image if you built it with a different name or want a different tag:

```powershell
docker tag <LOCAL_IMAGE_ID_or_NAME> <DOCKERHUB_USERNAME>/coffee-artistry:1.0.0
```

3. Push the image to Docker Hub:

```powershell
docker push <DOCKERHUB_USERNAME>/coffee-artistry:latest
```

After pushing, the image will be available at https://hub.docker.com/r/<DOCKERHUB_USERNAME>/coffee-artistry

Official public image
---------------------

If you want to use the already-published image for demos, there is a public image available at:

https://hub.docker.com/repository/docker/aftab2010/coffee-artistry/

You can pull it directly with:

```powershell
docker pull aftab2010/coffee-artistry:latest
```

## Minimal GitHub Actions example (optional)

Add this to `.github/workflows/docker-publish.yml` to build and push the image on every push to main (requires `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets configured in the repository settings).

Note: `DOCKERHUB_TOKEN` should be a Docker Hub access token (recommended) created from your Docker Hub account (Account Settings → Security → New Access Token). While you can use your Docker Hub password, using a dedicated personal access token for CI is more secure and easier to revoke.

```yaml
name: Build and Push Docker image

on:
	push:
		branches: [ main ]

jobs:
	build-and-push:
		runs-on: ubuntu-latest
		steps:
			- uses: actions/checkout@v4
			- name: Build the image
				run: docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/coffee-artistry:latest .
			- name: Log in to Docker Hub
				# Use the token stored in the repository secrets. This should be a Docker Hub access token (or password).
				run: echo ${{ secrets.DOCKERHUB_TOKEN }} | docker login -u ${{ secrets.DOCKERHUB_USERNAME }} --password-stdin
			- name: Push the image
				run: docker push ${{ secrets.DOCKERHUB_USERNAME }}/coffee-artistry:latest
```

## Cleanup (remove image locally)

```powershell
docker rmi <DOCKERHUB_USERNAME>/coffee-artistry:latest
```

If the image is referenced by stopped containers, remove those containers first.

## Troubleshooting

- "docker: command not found" — install Docker and ensure the daemon/service is running.
- Login/push fails — ensure your Docker Hub username and password/token are correct. For CI use a token rather than a password.
- Port already in use — change the host port when running (e.g., `-p 9090:80`).

## Notes and next steps

- The provided `Dockerfile` is intentionally simple and small (based on `nginx:alpine`). For production images you may want to add caching headers, a custom Nginx config, or an automated build pipeline.
- To publish an official image name, create and push tags like `1.0.0` and `latest` and enable automated builds on Docker Hub or use a CI workflow like the GitHub Actions example above.

---

Happy containerizing! If you want, I can also add the GitHub Actions workflow file and a short script to automate build-and-push locally.
