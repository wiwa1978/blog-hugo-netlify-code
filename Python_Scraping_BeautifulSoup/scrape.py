from bs4 import BeautifulSoup
from urllib.request import urlopen

url="https://www.imdb.com/chart/top"
page=urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

data = []
info = []
table = soup.find('table', attrs={'class':'chart'})
table_body = table.find('tbody')

rows = table_body.findAll('tr')
for row in rows:
   cols = row.findAll('td')
   for item in cols:
      text = item.find('a', href=True)
      if text:
         #print(text.get_text())
         data = text.get_text().rstrip()
         info.append(data)

i = 1
for item in info:
   if item:
      print(str(i) + ": "+ item)
      i  = i + 1
   

