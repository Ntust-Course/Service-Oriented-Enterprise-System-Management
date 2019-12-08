from typing import List

from models import Service


class ServiceRegistryController:
    serviceList: List[Service] = [
        Service(name="Registry", location="myprotocol:myip:myport")
    ]

    def get(self) -> List[Service]:
        return self.serviceList

    def post(self, service: Service):
        self.serviceList.append(service)

    def delete(self, serviceName: str):
        self.serviceList.remove(
            next(filter(lambda s: s.name == serviceName, self.serviceList))
        )


ServiceRegistryController().delete("Registry")
print(ServiceRegistryController().get())
