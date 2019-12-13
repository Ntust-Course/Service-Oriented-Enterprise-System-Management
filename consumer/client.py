from zeep import Client

wsdl = "http://www.soapclient.com/xml/soapresponder.wsdl"
client = Client(wsdl=wsdl)
print(client.service.Method1("First", "Second"))

