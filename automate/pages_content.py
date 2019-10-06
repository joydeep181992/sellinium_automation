import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import re
import json
import sys

links = []

with open('links.txt', 'r') as r:
    line = r.readlines()
    for l in line:
        links.append(l.strip())

# print(links)

# url = "https://www.jlevinlaw.com/Criminal-Defense/DUI-DWI.shtml"
def get_content():
    return soup.find_all('div', attrs={'class': 'column-main'})

web_page = []
for link in links:
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    web = web_byte.decode('utf-8')

    soup = bs(web, 'html5lib')
    # soup.prettify()
    web_page.append(get_content())

# print(web_page)

# s = []
# for web in web_page:
#     soup = bs(web, 'html5lib')
#     # soup.prettify()
#     s.append(get_content())
# print(json.dumps(web_page, separators=(',', ':')))

# print(web_page[0][0])
json_object = []
for i in range(0, len(web_page)):
    json_object.append({
        "h1": str(web_page[i][0].h1),
        "content": str(web_page[i][0].article)
    },)

a = json.dumps(json_object, separators=(',', ':'), indent=4)

print(a)

with open('content.json', 'w', encoding="utf-8") as fs:
    fs.write(str(a))

# for i in range(0, len(web_page)):
#     json_object['h1'] = web_page[i][0].h1
#     json_object['content'] = web_page[i][0].content

# print(json_object)