import requests, re, os
from concurrent.futures import ThreadPoolExecutor

base_url = 'https://www.zhuangbi.info/?page=%s'

image_url_reg = r'a class="download-link" href="(.*?)" data-picture-id='
image_path = os.path.join(os.getcwd(), 'image')


def down_file(url):
    try:
        r = requests.get(url)
        with open(os.path.join(image_path, url.split('-')[-1]), 'wb') as f:
            f.write(r.content)
            print(url, "下载成功")
    except Exception as e:
        print(url, "下载失败")


pool = ThreadPoolExecutor(max_workers=10)
if __name__ == '__main__':
    for page in range(1, 83):
        result = requests.get(base_url % page)
        for image_url in re.findall(image_url_reg, result.text):
            pool.submit(down_file, image_url)
    pool.shutdown()