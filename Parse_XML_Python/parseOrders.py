import xmltodict

with open('sample.xml') as f:
   xml_content = f.read()

xml_dict = xmltodict.parse(xml_content)

customers = xml_dict['Root']['Customers']
orders = xml_dict['Root']['Orders']
#print(orders)
customer_list = []
for customer in customers['Customer']:
   customer_list.append(customer['@CustomerID'])
   
for customer in customer_list: 
   print(f"Orders for: {customer}")
   for order in orders['Order']:
      if(customer == order['CustomerID']):
         print(f"  ==>Employee {order['EmployeeID']} placed an order on {order['OrderDate']}")
         

