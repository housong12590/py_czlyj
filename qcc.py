import requests, re, json
from urllib import parse

# from sqlalchemy import Column, String, create_engine

start_url = 'http://www.qichacha.com/search_index?key=%25E9%25A3%259F%25E5%2593%2581&ajaxflag=1&province=JS&city=1&tel=T&statusCode=10&p={0}&'

headers = {
    'Cookie': '_uab_collina=150997654636256503075966; acw_tc=AQAAAE+qXhOgHAYAWoOVJFgr3NPEsrjb; hasShow=1; _umdata=2FB0BDB3C12E491D898B7FF5457DC6F6606AADC154B339B14C53F2A958190BE2C5CD238CF1989958CD43AD3E795C914CFE9A8D285B7F0C199B6C79561C463266; PHPSESSID=6tgg1i5f3r745c6vtllf036836; zg_did=%7B%22did%22%3A%20%2215f919d60f75c5-0551dfa9556817-5b4a2c1d-1fa400-15f919d60f889f%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201510760876763%2C%22updated%22%3A%201510763801963%2C%22info%22%3A%201510756663973%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%225431e87b22de8d2050a3740fc6273ea4%22%7D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Upgrade-Insecure-Requests': "1",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'www.qichacha.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest'
}

item_span_regexp = re.compile(r'<tr>([\s\S]*?)</tr>')
q_name_regexp = re.compile(r'<td> <a href="/.*?class="ma_h1">(.*?)</a><br/>')
phone_regexp = re.compile(r'\s+电话：(.*?)\n')
p_name_regexp = re.compile(r'<a class="a-blue" href=.*?">(.*?)</a>')
register_money_regexp = re.compile(r'注册资本：(.*?)</span>')
register_time_regexp = re.compile(r'成立时间：(.*?)</span>')
keyword_regexp = re.compile(r'<em>(.*?)</em>')
status_regexp = re.compile(r'<span class="ma_cbt_green m-l-xs">(.*?)</span>')
scope_regexp = re.compile(r'<i class="i\s+i-search"></i>(.*?)</p>')

max_page_regexp = re.compile(r'<span class="text-danger">(\s.*?)\+\s+</span>')

result_list = []

f_text = parse.unquote(requests.get(start_url.format(1), headers=headers).content.decode('utf-8'))

max_page = re.findall(max_page_regexp, f_text)[0].replace(' ', '')


def get_value(reg, item):
    try:
        return re.findall(reg, item)[0]
    except Exception as e:
        # print(e)
        return ""


temp_list = []


def get_html_content(url):
    print(url)
    result = requests.get(url, headers=headers)
    return parse.unquote(result.content.decode('utf-8'))


def parse_content(content):
    obj_list = []
    for item in re.findall(item_span_regexp, content):
        # print(item)
        obj = {
            'q_name': get_value(q_name_regexp, item).replace('<em>', '').replace('</em>', ''),
            'phone': get_value(phone_regexp, item),
            'p_name': get_value(p_name_regexp, item),
            'register_money': get_value(register_money_regexp, item),
            'register_time': get_value(register_time_regexp, item),
            'keyword': get_value(keyword_regexp, item),
            'status': get_value(status_regexp, item)}
        obj_list.append(obj)
    return obj_list


def check_result(list, url):
    if len(list) == 0 and url not in temp_list:
        temp_list.append(url)



def xx():
    for url in temp_list:
        content = get_html_content(request_url)
        ls = parse_content(content)
        check_result(ls, url)
        result_list.extend(ls)


if __name__ == '__main__':
    for index in range(1, int(max_page)):
        request_url = start_url.format(index)
        content = get_html_content(request_url)
        ls = parse_content(content)
        # check_result(ls, request_url)
        result_list.extend(ls)
        # xx()
    # print(len(result_list))

    with open('qccresult.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(result_list, ensure_ascii=False))

print(len(result_list))