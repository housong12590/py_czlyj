import urllib.request
import urllib.error
import os

import pdfkit
from bs4 import BeautifulSoup

url = 'http://mobile.umeng.com/apps/d26100ed44dab88e6c49e195/reports/realtime_summary'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'Cookie': "um_lang=zh; cna=KoYRErplvRwCAbRmG6WELOoc; umengplus_name=304536797%40qq.com; umplusuuid=7bd78ddee02ac4312b7ed1ebf76d25f9; umplusappid=umeng; __ufrom=http://mobile.umeng.com/analytics; umlid_575ec6a467e58ec53b0022af=20170920; isg=AiMjFkInfsjlnDL8QYlrJe24smcNsLbYABQle1WApQL5lEK23evVq-3E-FJh; pgv_pvi=2168085504; pgv_si=s6718537728; _ga=GA1.2.363121577.1505887340; _gid=GA1.2.616333715.1505887340; ummo_ss=BAh7CUkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjoGRVRbCEkiCVVzZXIGOwBGWwZvOhNCU09OOjpPYmplY3RJZAY6CkBkYXRhWxFpXGljaQHGaQGkaWxpAeVpAY5pAcVpQGkAaSdpAa9JIhlPSFoySGxqSHFMZG5pcWpXanJveAY7AFRJIg91bXBsdXN1dWlkBjsARiIlN2JkNzhkZGVlMDJhYzQzMTJiN2VkMWViZjc2ZDI1ZjlJIg9zZXNzaW9uX2lkBjsAVEkiJTIzYzA3NzM1NTg3YTZkMWViZjM1YzUwYzdkYTlkODg0BjsARkkiEF9jc3JmX3Rva2VuBjsARkkiMWJQc0d4MDN4TkVKU2ttSmF1K0Z2OTIvMnZ3SFJxMG5MQ3Faa2JsNTNaUFk9BjsARg%3D%3D--d38ea2b6ebf7200270afa164dd22a787e104e65d; __utma=151771813.2058658665.1502847861.1504055314.1505887292.6; __utmb=151771813.30.9.1505887954326; __utmc=151771813; __utmz=151771813.1502847861.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
}
req = urllib.request.Request(url, None, headers)
resp = urllib.request.urlopen(req).read()
with open("umeng.html", "wb+") as f:
    f.write(resp)
print(resp)
