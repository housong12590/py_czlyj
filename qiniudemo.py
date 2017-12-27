from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import http
import os
from urllib import request

access_key = 'T3MasEjXJ-bNYueJB5Pc8zIulcbdOfJK1CW6oDUS'
secret_key = 'xamgaJxWklW4NFaM5INYaVqsUYT-CubVU6zc8yLf'
bucket_name = 'pss123546'


parent_path = 'C:/Users/Administrator/Desktop/qiniuimage'
local_files = os.listdir(parent_path)
r = Auth(access_key, secret_key)
# for file in local_files:
#     token = request.upload_token(bucket_name, file)

#     print(info)


host = 'http://rs.qbox.me'
url = host + '/buckets'
token = r.token_of_request(url)
authorization = 'QBox {}'.format(token)
headers = {
    'Authorization': authorization
}
req = request.Request(url, headers=headers)
result = request.urlopen(req).read()
print(result)
