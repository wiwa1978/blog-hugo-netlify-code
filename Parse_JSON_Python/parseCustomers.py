import json

with open('sample.json') as f:
   json_content = f.read()


json_dict = json.loads(json_content)
#print(type(json_dict))

customers = json_dict['Customers']
#
print(customers)

for customer in customers['Customer']:
   print(f"Customer ID: {customer['@CustomerID']}")
   print(f"Company Name: {customer['CompanyName']}")
   print(f"Contact Name: {customer['ContactName']}")
   print(f"  ==>  Street: {customer['FullAddress']['Address']}")
   print(f"  ==>  City: {customer['FullAddress']['City']}")
   print(50* "-")


