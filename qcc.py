import requests, re, json
from urllib import parse
import time


start_url = 'http://www.qichacha.com/search_index?key={0}&ajaxflag=1&province=JS&city=1&tel=T&statusCode=10&p={1}&'

headers = {
    'Cookie': 'acw_tc=AQAAAFM6hW4dhgIAAjtNMdowya/OAXGd; hasShow=1; _uab_collina=151119887507162310001182; _umdata=6AF5B463492A874D84C37624E73A40FEE2C977CE17C22255DD7BF9DF1D28AC1020FF79A36E682A4BCD43AD3E795C914C3E1FD640964304002FAFCE67D91C8AFA; PHPSESSID=l4hmasdfhnjj9u6k6s5l34hus6; zg_did=%7B%22did%22%3A%20%2215fda78c16d362-0a62abb5c6696e-5b4a2c1d-144000-15fda78c16e28a%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201511198867826%2C%22updated%22%3A%201511198940404%2C%22info%22%3A%201511198867830%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22db20066dff91ee0bcea40e5e25e99847%22%7D',
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


# f_text = parse.unquote(requests.get(start_url.format(1), headers=headers).content.decode('utf-8'))


# max_page = re.findall(max_page_regexp, f_text)[0].replace(' ', '')


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


def xxx(url):
    content = get_html_content(url)
    time.sleep(2)
    try:
        re.findall(item_span_regexp, content)[0]
    except:
        fid_list.append(url)
        print(url, '请求失败')
    ls = parse_content(content)
    result_list.extend(ls)


fid_list = []

if __name__ == '__main__':
    for index in range(1, int(11)):
        request_url = start_url.format(parse.quote("化妆品"), index)
        xxx(request_url)

    for url in fid_list:
        xxx(url)
    with open('huazhuangping.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(result_list, ensure_ascii=False))

print(len(result_list))
