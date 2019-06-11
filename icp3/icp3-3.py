import requests
from bs4 import BeautifulSoup
import os

contentdoc = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(contentdoc.content,'html.parser')
print(soup.title.string)
for link in soup.findAll('a'):
    print(link.get('href'))


