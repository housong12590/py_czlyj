import urllib.request
import re
import json
import urllib.parse
from bs4 import BeautifulSoup
import pymysql

reg_money = r'注册资本：?(\S*)</span>'
reg_time = r''
reg_phone = r''
reg_email = r''
reg_address = r''

# db = pymysql.connect('localhost', 'czlyj', '123546', 'CZLYJDB')


# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""



def htmlDownload(url, headers={}):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    req.add_header("Cookie",
                   "acw_tc=AQAAAGbyzmM8oA4AD3tutAwzVZBQkeRx; hasShow=1; _uab_collina=150296049022604980074033; _umdata=0823A424438F76AB025DBBCBFEA83FB2C6666421860863757B74D33C7EE688AFE45D7F48E5B5C63ECD43AD3E795C914C8397460F4EF6FB49F094A5B4502C8BAA; PHPSESSID=q7e2hb764gffpnh8l14iuq9oe3; zg_did=%7B%22did%22%3A%20%2215def6d0afa625-0dce6ed8be6461-36624308-1fa400-15def6d0afbb6c%22%7D; zg_3aa6aa556adf4e08a0542535203c5526=%7B%22sid%22%3A%201502960487165%2C%22updated%22%3A%201502964629426%2C%22info%22%3A%201502960487167%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%2234f4cf345b11d18eba28d55fed9f011a%22%7D")
    page = urllib.request.urlopen(req)
    return page.read()


def HtmlParse(html, mode="lxml"):
    all_list = []
    soup = BeautifulSoup(html, mode)
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
        money = span_list[0].get_text()
        print(money)

        # 成立时间
        time = span_list[1].get_text().strip()
        print(time)

        # 电话号码
        phone = p_list[1].get_text().strip('\n').split('\n')[0]
        print(phone)

        # 邮箱
        email = p_list[1].find("span").get_text()
        print(email)

        # 地址
        address = p_list[2].get_text().strip()
        print(address)

        # # 经营范围
        # range = p_list[3].get_text()
        # print(range)

        # 企业状态
        status_td = td_list[2]
        status = status_td.find("span").get_text()
        print(status)

        # cursor = db.cursor()


        dict1 = {"company_name": company_name, "legal_name": legal_name, "money": money, "create_time": time,
                 "phone": phone, "email": email, "address": address, "status": status}
        all_list.append(dict1)
    return all_list


def saveToFile(data, path):
    file = open(path, "w+")
    file.write(data)
    file.close()
    pass


# base_url = "http://www.qichacha.com/search_index?key=%25E5%25BB%25BA%25E7%25AD%2591&ajaxflag=1&&&p=1&province=JS&city=1&"
base_url = "http://www.qichacha.com/search?key=%E5%BB%BA%E7%AD%91"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
# key = '建筑'
# value = {
#     'key': key,
#     'ajaxflag': '1',
#     'p': '1',
#     'province': 'JS',
#     'city': '1'
# }

html = htmlDownload(base_url, headers)
data = HtmlParse(html)
j = json.dumps(data)
str = urllib.parse.unquote(j)

saveToFile(str, "data.json")
# print(data)
