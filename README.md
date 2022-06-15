# inflation.ninja-backend
Flask backend for inflation.ninja

## Interactive Shell

* `docker images`
* `docker run -it <image id> sh`

## Endpoint
Exposed locally at `http://172.17.0.2:8080`

## Deploying on AWS Lightsail
# TODO: just use docker hub container service
```
aws lightsail create-container-service --service-name flask-service --power small --scale 1
```

```
aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container
```

```
aws lightsail create-container-service-deployment --service-name flask-service --containers file://containers.json --public-endpoint file://public-endpoint.json
```