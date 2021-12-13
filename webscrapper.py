from bs4.dammit import html_meta
import requests
from bs4 import BeautifulSoup

URL = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020"
page = requests.get(URL)

soup = BeautifulSoup(page._content, 'html.parser')

#print(soup.prettify())
#print(soup.title.find_all)
#print(soup.title.string)
#print(soup.text.strip())
"""
tables = soup.findAll("table")

for table in tables:
     if table.findParent("table") is None:
        print(str(table))
"""

"""
tables1 = soup.findAll("table",limit=2)

for table in tables1:
     if table.findParent("table") is None:
        print(str(table))
"""

#tab=soup.find("table",{"class":"wikitable"})
#print(tab.prettify())
"""
links = [a['href'] for a in soup.find_all('a', href=True,limit=5)]

print(links)"""

# find all table ,get the first
table = soup.find_all('table', class_="wikitable")[0]  # Only use the first table
# iter over it
for record in table.findAll('tr'):
    #print(record)
    for data in record.findAll('td'):
        #print(data)
        for a in data.find_all('a', href=True,title=True):
            print(f"URL: {a['href']}, Club:{a['title']}")