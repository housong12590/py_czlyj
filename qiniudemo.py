from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os

access_key = 'T3MasEjXJ-bNYueJB5Pc8zIulcbdOfJK1CW6oDUS'
secret_key = 'xamgaJxWklW4NFaM5INYaVqsUYT-CubVU6zc8yLf'
bucket_name = 'pss123546'

# os.listdir('C:/Users/Administrator/Desktop/qiniuimage')
parent_path = 'C:/Users/Administrator/Desktop/qiniuimage'
local_files = os.listdir(parent_path)
request = Auth(access_key, secret_key)
for file in local_files:
    token = request.upload_token(bucket_name, file)
    ret, info = put_file(token, file, parent_path + "/" + file)
    print(info)
