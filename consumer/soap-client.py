from zeep import Client

wsdl = "http://localhost:8002/soap?wsdl"
client = Client(wsdl=wsdl)
print(client.service.get_inventory())
