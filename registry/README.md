# Service Registry

## Build image

```bash
docker build . -t sheiun/soa-registry
```

## Run image

```bash
docker run -d -p 5000:5000 --name registry sheiun/soa-registry python app.py
```
