import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777',
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777'
}
   
url= "https://www.amazon.in"

r = requests.get(url, proxies=proxies)

soup = BeautifulSoup(html_doc, "html.parser")