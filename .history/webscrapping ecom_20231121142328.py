import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777',
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777'
}

    r = requests.get(url, proxies=proxies)
    
url= "https://www.spicejet.com/"

fetchAndSaveToFile(url, "data/times.html")

soup = BeautifulSoup(html_doc, "html.parser")