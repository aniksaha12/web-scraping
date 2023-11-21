import requests

proxies = {
    # "http": "http://10.10.1.10:3128", 
    # "http": "http://10.10.1.10:1080",
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777',
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777'
}

r = requests.get("https://api64.ipify.org?format=json" , proxies=proxies)

print(r.json())