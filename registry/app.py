from flask import Flask, jsonify, request
from flask.views import MethodView

from controller import ServiceRegistryController
from models import Service


class RegistryAPI(MethodView):
    def get(self):
        return jsonify(ServiceRegistryController.get())

    def post(self):
        ServiceRegistryController.post(Service.from_form(request.form))
        return self.get()

    def delete(self):
        ServiceRegistryController.delete(request.form["name"])
        return self.get()


app = Flask(__name__)
app.url_map.strict_slashes = False

app.add_url_rule("/api/registry", view_func=RegistryAPI.as_view("registry"))

app.run(host="0.0.0.0")
