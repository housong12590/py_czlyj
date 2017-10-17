import urllib.request
import urllib.error
import os

import pdfkit
from bs4 import BeautifulSoup

base_url = "http://www.runoob.com"
path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 安装位置
config = pdfkit.configuration(wkhtmltopdf=path_wk)


def get_html_content(url):
    try:
        print("request url ->" + url)
        html = urllib.request.urlopen(url).read()
        return html
    except Exception as e:
        print(e)
        return None


def get_url_list(html):
    soup = BeautifulSoup(html, "lxml")
    urls = list()
    for a in soup.find_all("a", {"target": "_top"}):
        title = a['title']
        url = base_url + a['href']
        print(url)
        urls.append(url)
        # print({title, url})
    return urls


def parse_html_content(url):
    html = get_html_content(url)
    soup = BeautifulSoup(html, "lxml")
    result = soup.find("div", {"class": "article-body"})
    for img in soup.findAll("img"):
        imgurl = img['src']
        if imgurl.startswith('//www.runoob.com/'):
            imgurl = "http:" + imgurl
            img['src'] = imgurl[49:]
            dir = os.path.abspath('./images')
            work_path = os.path.join(dir, imgurl[49:])
            urllib.request.urlretrieve(imgurl, work_path)
    return result


def main():
    start_url = base_url + "/kotlin/kotlin-tutorial.html"
    html = get_html_content(start_url)
    f = open("kotlindoc.html", "ab")
    for url in get_url_list(html):
        print("获取内容 -> " + url)
        html = parse_html_content(url)
        print(html)
        try:
            f.write(html.encode("utf-8"))
        except Exception as e:
            print("解析失败-> " + str(e))
        print("解析并写成完成....")
    # html = parse_html_content(start_url)
    # html = html.encode("utf-8")

    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }

    # with open("text.html", "ab") as f:
    #     f.write(html)
    print("开始转换PDF...请稍候")
    pdfkit.from_file("kotlindoc.html", "G://kotlindoc.pdf", configuration=config, options=options)
    print("PDF 转换完成")


if __name__ == "__main__":
    main()
