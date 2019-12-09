from flask import jsonify, request
from flask.views import MethodView

from controllers import ServiceRegistryController
from models import Service


class RegistryView(MethodView):
    def get(self):
        return jsonify(ServiceRegistryController.get())

    def post(self):
        ServiceRegistryController.post(Service.from_form(request.form))
        return self.get()

    def delete(self):
        ServiceRegistryController.delete(request.form["name"])
        return self.get()
