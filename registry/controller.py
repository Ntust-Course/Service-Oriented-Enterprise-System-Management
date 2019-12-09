from dataclasses import asdict
from typing import Dict, List

from models import Service


class ServiceRegistryController:
    service_list: List[Service] = [
        Service(name="Registry", location="myprotocol://myip:myport")
    ]

    @classmethod
    def get(cls) -> List[Dict[str, str]]:
        return list(map(asdict, cls.service_list))

    @classmethod
    def post(cls, service: Service):
        cls.service_list.append(service)

    @classmethod
    def delete(cls, service_name: str):
        cls.service_list.remove(
            next(filter(lambda s: s.name == service_name, cls.service_list))
        )
