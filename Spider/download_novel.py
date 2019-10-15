import requests
import sys
from bs4 import BeautifulSoup

# 定义一个结构体


class download_novel(object):

        # 初始化函数
    def __init__(self):

        # 之后提取网页需要加上的部分
        self.begin = "http://www.biqukan.com"
        # 小说章节所在的网页
        self.target_url = "http://www.biqukan.com/3_3042/"
        # 定义一个存储小说网页的空列表，用于保存迭代后的每章小说的网址
        self.target_urls = []
        # 定义一个存储小说每章题目的空列表
        self.title = []
        # 定义一个变量存储小说的章数，用于最后输出
        self.nums = 0

    # 定义一个函数，获取每章的题目和下载的网址
    def get_download_url(self):

        # 请求小说题目所在的网站
        res = requests.get(url=self.target_url)
        # 利用lxml剖析网页
        soup = BeautifulSoup(res.text, "lxml")
        # 找到包含所有题目的元素
        result = soup.find_all('div', class_="listmain")
        # 提取result中所有的超链接
        a_list = BeautifulSoup(str(result[0]), "lxml").find_all('a')
        # 切片，除掉前面不需要的部分
        self.nums = len(a_list[12:])
        # 开始迭代页面
        for each in a_list[12:]:
                # 将每章小说的题目添加到title空列表中
            self.title.append(each.string)
            # 将每章小说的网址添加到target_urls空列表中（提取出来的只有一部分，需要加上self.begin才能构成完整的网站）
            self.target_urls.append(self.begin + each.get('href'))

    # 获取当前这章小说的内容
    def get_content(self, url):

        # 请求页面
        res = requests.get(url=url)
        # 利用lxml剖析网页
        soup = BeautifulSoup(res.text, "lxml")
        # 找到包含内容的元素
        result = soup.find_all('div', class_="showtxt")
        # 去掉内容前面的换行与空格
        texts = result[0].text.replace('\xa0' * 8, '\n')
        # 打印当前url网页中小说内容（一个章节）
        # print(texts)
        return texts

    def write_content(self, name, path, text):

        # write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":

    novel = download_novel()
    novel.get_download_url()
    print("遮天开始下载...")
    for i in range(novel.nums):
        novel.write_content(
            novel.title[i], '遮天.txt', novel.get_content(novel.target_urls[i]))
        sys.stdout.write("已下载: %.3f%%" % float(i * 100 / novel.nums) + '\r')
        sys.stdout.flush()
    print("遮天下载完成")
