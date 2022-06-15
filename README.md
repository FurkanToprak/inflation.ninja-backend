# inflation.ninja-backend
Flask backend for [inflation.ninja](www.inflation.ninja), deployable on AWS Lightsail via Docker.

### Objective

I made this server as a way to scrape stock data from free stock APIs and to cache the results as required. This way, I can keep updated versions of stock quotes and provide thousands of users with up-to-date market information _without_ having to buy a premium API account with higher API rates.

### Architecture

* Python3.10 backend that makes API calls to AlphaVantage to get stock information. This data is then processed, compressed, and cached.

* These methods are exposed through Flask GET endpoints.
    * `/`: Health check endpoint that returns `Hello, World!`.
    * `/getStock?ticker=<STOCK>`: Endpoint that returns the daily stock quote of the stock.
    * * `/getTopStocks`: Endpoint that returns some of the stocks that were traded with the highest volume. Unfortunately, this is a hard-coded list of stocks (for now).

* This Flask service lives in a Docker container (Alpine image). You can see the `scripts/` directory to build and run the container. Look at the `Dockerfile` for more.

* This Docker container is then deployed on Amazon Lightsail.

## Interactive Shell

* `docker images`
* `docker run -it <image id> sh`

## Endpoint
Exposed locally at `http://172.17.0.2:8080`

## Deploying on AWS Lightsail

### Login to Docker Hub
`docker login`

### Build Docker Container
`./scripts/build_docker.sh`

### Tag container
`docker tag inflation-ninja-backend furkantoprak/inflation-ninja-backend`

### Push to Docker Hub
`docker push furkantoprak/inflation-ninja-backend`

### Deploy Container on AWS Lightsail
`https://lightsail.aws.amazon.com/ls/webapp/home/containers`

## Local Development
### Kill Container Locally
`docker container list` and `docker container kill <id>`