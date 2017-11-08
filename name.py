import requests, re, os, json

base_url = 'http://www.resgain.net/netname_42_%s.html'

name_reg = r'<div class="btn btn-link btn1" title="双击可拷贝网名:(.*?)">.*</div>'

name_list = []
for index in range(13):
    result = requests.get(base_url % index)
    for name in re.findall(name_reg, result.text):
        if len(name) < 6:
            name_list.append(name)
            # print(name)
        else:
            print(name, '名字超长')
result = json.dumps(name_list, ensure_ascii=False)
with open('name.json', 'w', encoding='utf-8') as f:
    f.write(result)
