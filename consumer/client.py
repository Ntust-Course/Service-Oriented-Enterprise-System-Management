from zeep import Client

wsdl = "http://localhost:5000/soap?wsdl"
client = Client(wsdl=wsdl)
print(client.service.get_balance())

