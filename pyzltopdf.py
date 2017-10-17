import urllib.request
import urllib.error
import os

import pdfkit
from bs4 import BeautifulSoup

base_url = "https://www.liaoxuefeng.com"
path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 安装位置
config = pdfkit.configuration(wkhtmltopdf=path_wk)


def get_page_content(url):
    try:
        print("request url ->" + url)
        html = urllib.request.urlopen(url).read()
        return html
    except Exception as e:
        print(e)
        return None


i = 0


def get_url_list(html):
    soup = BeautifulSoup(html, "lxml")
    urls = list()
    for li in soup.find("ul", {'class': 'uk-nav uk-nav-side', 'style': 'margin-right:-15px;'}).findAll("li"):
        title = li.find("a").get_text()
        url = base_url + li.find("a")['href']
        urls.append([title, url])
    print("获取所有URL完成 一共->" + str(len(urls)) + "个")
    return urls


def get_html_content(url, title):
    html = get_page_content(url)
    soup = BeautifulSoup(html, "lxml")
    result = soup.find("div", {"class": "x-wiki-content x-main-content"})
    center_tag = soup.new_tag("center")
    title_tag = soup.new_tag('h1')
    title_tag.string = title
    center_tag.insert(1, title_tag)
    result.insert(1, center_tag)
    for img in result.findAll("img"):
        imageurl = base_url + str(img['src'])
        global i
        i = i + 1
        new_image_name = str(i) + ".jpg"
        img['src'] = new_image_name
        dir = os.path.abspath('./images')
        work_path = os.path.join(dir, new_image_name)
        urllib.request.urlretrieve(imageurl, work_path)
    return result


def main():
    start_url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    start_html = get_page_content(start_url)
    datalist = get_url_list(start_html)
    f = open("test.html", 'ab+')
    for item in datalist:
        print(item[0])
        content = get_html_content(item[1], item[0])
        f.write(content.encode("utf-8"))

    f.close()
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
    pdfkit.from_file("test.html", "G://pydoc.pdf", configuration=config, options=options)
    print("PDF 转换完成")


if __name__ == "__main__":
    main()
