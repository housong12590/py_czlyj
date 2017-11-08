import re
import json
import random

text_list = []

reg = r'text="(.*?)"'
with open("layout.xml", 'r', encoding='utf-8') as f:
    content = str(f.read())
    for i in re.findall(reg, content):
        text_list.append(i)
        # print(i)
print(json.dumps(text_list, ensure_ascii=False))

anjingList = ["读书", "听音乐", "看报", "品茶", "乐器", "烹饪", "手工制作", "游戏", "收藏", "看电视", "网络分享", "咖啡",
              "写作", "书法绘画", "网上购物"]
r = random.randint(1, 5)
anjing = ''
for i in [random.randint(0, len(anjingList) - 1) for _ in range(r)]:
    anjing += '%s,' % anjingList[i]
print(anjing[0: len(anjing)-1])
