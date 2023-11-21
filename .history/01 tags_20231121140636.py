import requests
from bs4  import BeautifulSoup

with open("data/times.html", "r" ,encoding="utf-8") as f:
    html_doc = f.read()

# soup object   
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title, type(soup.title))
# print(soup.div)

def has_class_but_not_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

# results = soup.find_all(has_class_but_not_id)
results = soup.find_all(has_content)
for result in results:
    print(result, "\n\n")