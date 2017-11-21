import requests

result = requests.get(
    "http://shenhuanglive.oss-cn-shanghai.aliyuncs.com/Htm/Banner/kx_MiZNzhuy.html")
with open("jsread.html", 'wb') as f:
    f.write(result.content)
