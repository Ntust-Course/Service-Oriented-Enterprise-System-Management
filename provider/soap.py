from random import randint

from spyne import Application, Integer, Iterable, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from utils import INV, deregister, register


class InventoryService(ServiceBase):
    @rpc(_returns=Integer)
    def get_inventory(self):
        global INV
        INV -= randint(0, 100)
        return INV


application = Application(
    [InventoryService],
    "spyne.examples.hello.soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

wsgi_application = WsgiApplication(application)


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    server = make_server(host="0.0.0.0", port=8002, app=wsgi_application)
    try:
        register({"name": "inventory-soap", "url": "http://localhost:8002"})
        server.serve_forever()
    finally:
        deregister("inventory-soap")
