import requests
from urllib import parse
import json

host = 'http://192.168.0.14:5000/api/v1/%s'


def post(url, data):
    result = requests.post(url, data=data)
    return handle_result(result)


def handle_result(result):
    print('url->', result.url)
    text = format_json(result.text)
    return text


def format_json(content):
    text = json.loads(content, encoding='utf-8')
    print(json.dumps(text, indent=4, ensure_ascii=False))
    return text


def register(username, password):
    url = host % 'quato/users'
    data = {
        "mobile": username,
        "password": password
    }
    post(url, data)


def login(username, passwrod, type):
    pass


def change_password(id, oldpwd, newpwd):
    url = host % 'quato/user/%s/change_password' % id
    data = {
        'old_password': oldpwd,
        'password': newpwd
    }
    post(url, data)


def change_mobile(id, mobile, password):
    url = host % 'quato/user/%s/change_mobile' % id
    data = {
        'new_mobile': mobile,
        'password': password
    }
    post(url, data)


def batch(size, callback):
    url = host % 'quato/users/batch'
    data = {
        'size': size,
        'callback': callback
    }
    return post(url, data)


if __name__ == '__main__':
    pass
    # users = batch("3000", "1")
    # print(len(users['data']))
    # register("17602541064", '123456')
    # change_password('0fc8f610-cb6c-11e7-b80d-dca90481771e', "e444be071bfa4eeb38ca36f5fefac2fa", "e444be071bfa4eeb38ca36f5fefac2fa")
    # change_mobile('ee9cd058-cb70-11e7-889a-dca90481771e', '13776601078', 'e444be071bfa4eeb38ca36f5fefac2fa')
