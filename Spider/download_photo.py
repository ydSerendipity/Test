import requests
from bs4 import BeautifulSoup
# import lxml
import urllib
import os

BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []

# 迭代所有页面
for x in range(1, 1603):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)


def download_img(url):

    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('images', filename)
    # 将远程数据下载到本地的方法
    urllib.request.urlretrieve(url, filename=path)


def GET_PAGE(page_url):

    headers = {
        'Host': 'www.doutula.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36'
    }
    res = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    img_list = soup.find_all(
        'img', attrs={'class': 'img-responsive lazy image_dta'})
    for img in img_list:
        url = img['data-original']
        download_img(url)


def main():

    for page_url in PAGE_URL_LIST:
        GET_PAGE(page_url)

if __name__ == '__main__':
    main()
