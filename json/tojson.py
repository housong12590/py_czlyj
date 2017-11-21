import json

with open('shiping.json', encoding='utf-8') as f:
    with open('食品.txt', 'w', encoding='utf-8') as f1:
        f1.write(
            "---------------------------------------茶叶-----------------------------------------\n")
        for item in json.load(f):
            content = '%s    %s    %s \n' % (
                item['q_name'], item['phone'], item['p_name'])
            f1.write(content)
            # print(content)
