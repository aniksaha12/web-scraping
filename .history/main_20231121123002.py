import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path)
url= "https://book.spicejet.com/RetrieveBooking.aspx"

r = requests.get(url)
print (r.text)