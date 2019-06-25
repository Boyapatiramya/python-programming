import requests
from bs4 import BeautifulSoup
import os

contentdoc = requests.get("https://en.wikipedia.org/wiki/Google")
soup = BeautifulSoup(contentdoc.content,'html.parser')
print(soup.text)
file_name_dest = input("Enter the destination file name")
f=open(file_name_dest, "w+", encoding="UTF-8")
f.write(soup.text)
f.close()

