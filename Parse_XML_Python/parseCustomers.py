import xmltodict

with open('sample.xml') as f:
   xml_content = f.read()

print(xml_content)

xml_dict = xmltodict.parse(xml_content)
print(type(xml_dict))

customers = xml_dict['Root']['Customers']
print(customers)

for customer in customers['Customer']:
   print(f"Customer ID: {customer['@CustomerID']}")
   print(f"Company Name: {customer['CompanyName']}")
   print(f"Contact Name: {customer['ContactName']}")
   print(f"  ==>  Street: {customer['FullAddress']['Address']}")
   print(f"  ==>  City: {customer['FullAddress']['City']}")
   print(50* "-")

