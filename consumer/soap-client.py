from zeep import Client

wsdl = "http://localhost:6666/soap?wsdl"
client = Client(wsdl=wsdl)
print(client.service.get_inventory())
