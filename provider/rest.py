from random import randint

import requests
from flask import Flask, jsonify

from utils import INV, deregister, register

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/api/inventory", methods=["GET"])
def inventory():
    """simulate the current inventory"""
    global INV
    INV -= randint(0, 100)
    # NOTE: json or another response type
    return jsonify({"inventory": INV})


try:
    register({"name": "inventory-rest", "url": "http://localhost:8001"})
    app.run(host="0.0.0.0", port=8001)
finally:
    deregister("inventory-rest")
