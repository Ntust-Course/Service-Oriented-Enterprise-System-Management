import socket
from dataclasses import asdict
from typing import Dict, List

from models import Service

url_fmt = "{protocol}://{ip}:{port}"


class ServiceRegistryController:
    service_list: List[Service] = [
        Service(
            name="Registry",
            url=url_fmt.format(
                protocol="http",
                ip=socket.gethostbyname(socket.gethostname()),
                port="5000",
            ),
        )
    ]

    @classmethod
    def get(cls) -> List[Service]:
        return cls.service_list

    @classmethod
    def post(cls, service: Service):
        cls.service_list.append(service)

    @classmethod
    def delete(cls, service_name: str):
        cls.service_list.remove(
            next(filter(lambda s: s.name == service_name, cls.service_list))
        )
