import urllib.request
import urllib.error
import os

import pdfkit
from bs4 import BeautifulSoup

url = "https://juejin.im/post/59bf91476fb9a00a583178d3"

resp = urllib.request.urlopen(url).read()
soup = BeautifulSoup(resp, "lxml")
result = soup.find("div", {"class": "columen-view-main"})
with open("jianshu.html", "ab+") as f:
    f.write(result)
print(result)
