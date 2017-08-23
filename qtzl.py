from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import json
import sys
import re
import qtzlsql


def get_page_content(url):
    html = urllib.request.urlopen(url).read()
    return html


re_title = re.compile(r'Qt 学习之路 2（\d+）：([\S\s]+)')


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    for li in soup.find("div", {'class': 'thecontent clearfix'}).find("ol").find_all('li'):
        title = li.find('a').get_text()
        url = li.find('a').attrs['href']
        if url.endswith("/"):
            url = url[:len(url) - 1]
        item = {"title": title, "url": url}
        # item = (title, url)
        data.append(item)
        print(item)
        # for h2 in soup.find_all("div", {'class': 'thecontent clearfix'}):
        #     title = h2.find("a").get_text()
        #     url = h2.find("a").attrs['href']
        #     item = {"title:": title, "url": url}
        #     print(item)
        #     data.append(item)
        # return data


data = []


def main():
    # url = 'https://www.devbean.net/category/qt-study-road-2/page/{0}/'
    url = 'https://www.devbean.net/2012/08/qt-study-road-2-catelog/'
    html = get_page_content(url)
    parse_html(html)
    # for index in range(1, 11):
    # html = get_page_content(url.format(str(index)))
    # parse_html(html)

    # data.reverse()
    # f = open("qtzl.json", "w")
    # f.write(json.dumps(data, ensure_ascii=False))
    # f.close()
    qtzlsql.insert(data)


if __name__ == '__main__':
    main()
