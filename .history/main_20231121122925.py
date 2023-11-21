import requests

def fetchAndSaveToFile(url, path):
    r
url= "https://book.spicejet.com/RetrieveBooking.aspx"

r = requests.get(url)
print (r.text)