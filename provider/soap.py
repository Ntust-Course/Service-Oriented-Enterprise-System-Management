from random import randint

from spyne import Application, Integer, Iterable, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

INV = 10000


class InventoryService(ServiceBase):
    @rpc(_returns=Integer)
    def get_balance(self):
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

    server = make_server(host="127.0.0.1", port=5000, app=wsgi_application)
    server.serve_forever()
