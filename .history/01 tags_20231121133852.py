import requests
from bs4  import BeautifulSoup

with open("data/times.html", "r") as f:
    html_doc = f.read()

# soup object   
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
# print(soup.title)