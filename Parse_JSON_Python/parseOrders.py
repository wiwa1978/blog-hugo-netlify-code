import json

with open('sample.json') as f:
   json_content = f.read()

json_dict = json.loads(json_content)

customers = json_dict['Customers']
orders = json_dict['Orders']
#print(customers)
customer_list = []
for customer in customers['Customer']:
   customer_list.append(customer['@CustomerID'])

for customer in customer_list: 
   print(f"Orders for: {customer}")
   for order in orders['Order']:
      if(customer == order['CustomerID']):
         print(f"  ==>Employee {order['EmployeeID']} placed an order on {order['OrderDate']}")
         
