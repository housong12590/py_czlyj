import urllib.request
from bs4 import BeautifulSoup


def htmlDownload(url, data=None, headers={}):
    req = urllib.request.Request(url, data, headers)
    page = urllib.request.urlopen(req)
    return page.read()


def HtmlParse(html, mode="lxml"):
    soup = BeautifulSoup(html, mode)
    result = soup.find_all("tr")
    return result


def saveToFile(path):
    pass


base_url = "http://www.qichacha.com/search_index?key=%25E5%25BB%25BA%25E7%25AD%2591&ajaxflag=1&&&p=1&province=JS&city=1&"
header = {'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
datas = {

}
html = htmlDownload(base_url, datas, header)
data = HtmlParse(html)
print(data)
