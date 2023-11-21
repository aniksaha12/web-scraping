import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777',
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777'
}
   
url= "https://www.amazon.in/s?k=iphone&crid=1HDFNSMWVLXSE&sprefix=iphone%2Caps%2C231&ref=nb_sb_noss_1"

r = requests.get(url, proxies=proxies)

soup = BeautifulSoup(r.text, "html.parser")
