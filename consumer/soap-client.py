"""Deprecated with zeep"""
from suds.client import Client

c = Client("http://localhost:5000/soap?wsdl")
print(c.service.get_balance())
