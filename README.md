# inflation.ninja-backend
Flask backend for inflation.ninja

## Interactive Shell

* `docker images`
* `docker run -it <image id> sh`

## Endpoint
Exposed locally at `http://172.17.0.2:8080`

## Deploying on AWS Lightsail

### Build Docker Container
`./scripts/build_docker.sh`

### Tag container
`docker tag inflation-ninja-backend furkantoprak/inflation-ninja-backend`

### Login to Docker Hub
`docker login`

### Push to Docker Hub
`docker push furkantoprak/inflation-ninja-backend`

### Deploy Container on AWS Lightsail
`https://lightsail.aws.amazon.com/ls/webapp/home/containers`

## Local Development
### Kill Container Locally
`docker container list` and `docker container kill <id>`