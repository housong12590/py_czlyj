import urllib.request
import urllib.parse
import urllib.error
import json
import urllib.parse
import mysql
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
    data = []
    soup = BeautifulSoup(html, "lxml")
    try:
        tbody = soup.find("tbody")
        tr = tbody.find_all("tr")
        for t in tr:
            td_list = t.find_all("td")
            info_td = td_list[1]
            # 企业名称
            company_name = info_td.find("a").get_text()
            print(company_name)

            # 法人代表
            p_list = info_td.find_all("p")
            legal_name = p_list[0].find("a").get_text()
            print(legal_name)

            span_list = p_list[0].find_all("span")
            # 注册资本
            money = span_list[0].get_text()[5:]
            print(money)

            # 成立时间
            time = span_list[1].get_text().strip()[5:]
            print(time)

            # 电话号码
            phone = p_list[1].get_text().strip('\n').split('\n')[0][3:]
            print(phone)

            # 邮箱
            email = p_list[1].find("span").get_text()[3:]
            print(email)

            # 地址
            address = p_list[2].get_text().strip()[3:]
            print(address)

            # # 经营范围
            # range = p_list[3].get_text()
            # print(range)

            # 企业状态
            status_td = td_list[2]
            status = status_td.find("span").get_text()
            print(status)

            exp = (company_name, legal_name, money, time, phone, email, address, status)
            data.append(exp)
    except Exception as e:
        print("-----")
        pass
    return data


def main():
    p = 0
    for i in range(1):
        html = get_page_content("建筑", '32', '3201', str(19))
        print(html)
        f = open("test.html", "wb")
        f.write(html)
        f.close()
        # data = parse_html_content(html)
        # mysql.insert(data)


if __name__ == '__main__':
    main()
