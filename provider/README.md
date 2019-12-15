# Provider

Provide some services and informations for consumers.

## Prerequirements

- Python 3.6 +

## Rest

- `Flask` only

## Soap

- All in requriements

## TODO

- Integration rest and soap

## Build Image

```shell
docker build . -t sheiun/soa-provider
```

## Run Container

```shell
docker run -d -p <port>:<port> --name <name> --network soa sheiun/soa-provider python <app_name.py>
```
