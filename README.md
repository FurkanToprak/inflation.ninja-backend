# inflation.ninja-backend
Flask backend for inflation.ninja

## Interactive Shell

* `docker images`
* `docker run -it <image id> sh`

## Endpoint
Exposed locally at `http://172.17.0.2:8080`

## Deploying on AWS Lightsail
# TODO: just use docker hub container service

## Build and run Docker image
`./deployScript.sh`

## Tag container
`docker tag inflation-ninja-backend furkantoprak/inflation-ninjabackend`

## Login to Docker Hub
`docker login`

## Push to Docker Hub
`docker push furkantoprak/inflation-ninja-backend`

## Deploy Container on AWS Lightsail
`https://lightsail.aws.amazon.com/ls/webapp/home/containers`