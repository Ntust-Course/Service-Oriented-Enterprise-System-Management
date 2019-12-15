# Service Registry

Docker: <https://hub.docker.com/r/sheiun/soa-registry>

## Use official image

```bash
docker pull sheiun/soa-registry
```

## Create network

```bash
docker network create soa
```

## Build image yourself

```bash
docker build . -t sheiun/soa-registry
```

## Run image

```bash
docker run -d -p 5000:5000 --name registry sheiun/soa-registry python app.py
```

## Push to docker hub

```bash
docker push sheiun/soa-registry
```
