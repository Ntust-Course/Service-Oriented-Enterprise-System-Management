import requests

INV = 10000

REGISTRY_URL = "http://registry:5000/api/registry"


def register(service: dict):
    res = requests.post(REGISTRY_URL, service)
    if not res.ok:
        raise Exception(res.reason)
    print(f"=== {service['name']} registered at {service['url']} === ")


def deregister(name: str):
    requests.delete(REGISTRY_URL, data={"name": name})
    print(f"=== {name} deregistered ===")

