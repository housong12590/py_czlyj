import urllib.request
import urllib.parse
import urllib.error
import json
import urllib.parse
import pxbsql
from config import *
from bs4 import BeautifulSoup


def get_page_content(key, province="JS", city="1", page="1"):
    data = {
        'key': key,
        'page': page,
        'area.province': province,
        'area.city': city
    }
    headers = {
        'User-Agent': USER_AGENT,
        'Cookie': COOKIE
    }
    url = "http://www.qixin.com/search?" + urllib.parse.urlencode(data)
    print(url)
    try:
        req = urllib.request.Request(url, None, headers)
        resp = urllib.request.urlopen(req).read()
        return resp
    except urllib.error.URLError:
        print("请求错误")
        return None


def parse_html_content(html):
    soup = BeautifulSoup(html, "lxml")
    data = []
    i = 0
    for div in soup.findAll("div", {'class': 'col-xs-24 padding-v-1x margin-0-0x border-b-b4 company-item'}):
        name = div.find("a", {"title": '点击查看公司详情'}).get_text()
        person = div.find("div", {'class': 'legal-person'}).get_text()[6:]
        phone = ""
        try:
            phone = div.find("span", {'class': 'margin-r-1x'}).get_text()
        except Exception:
            phone = ""
        i += 1
        print(i)
        data.append((name, person, phone))
    return data


def main():
    p = 0
    for i in range(54, 500):
        html = get_page_content("食品", '32', '3201', str(i))
        data = parse_html_content(html)

        pxbsql.insert(data)


if __name__ == '__main__':
    main()
