from random import randint

import requests
from flask import Flask, jsonify

app = Flask(__name__)
app.url_map.strict_slashes = False

INV = 10000

REGISTRY_URL = "http://localhost:5000/api/registry"


@app.route("/api/inventory", methods=["GET"])
def inventory():
    """simulate the current inventory"""
    global INV
    INV -= randint(0, 100)
    return jsonify({"inventory": INV})


def register():
    res = requests.post(
        REGISTRY_URL, {"name": "inventory", "url": "http://inventory:5000"}
    )
    if not res.ok:
        raise Exception(res.reason)
    print("=== registered === ")


def deregister():
    requests.delete(REGISTRY_URL, data={"name": "inventory"})
    print("=== deregistered ===")


try:
    register()
    app.run(host="0.0.0.0", port=5001)
finally:
    deregister()
