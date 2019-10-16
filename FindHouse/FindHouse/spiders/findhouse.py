# -*- coding: utf-8 -*-

import scrapy
from ..items import FindhouseItem

#网址前面的部分
url_pre = "https://wh.fang.ke.com/loupan/pg"
#新建一个空列表用于后期保存网址
url_list = []

for i in range(1, 2):
    #拼接成完整的网址
    url = url_pre + str(i)
    #将网址添加到列表中，以便爬取的时候循环
    url_list.append(url)
    i += 1

class FindHouse(scrapy.Spider):
    #爬虫名，运行时候用到
    name = "zhaofang"
    #爬取的网站区域，这里start_urls后面的s不能掉，不然爬不到数据
    start_urls = url_list

    def parse(self, response):
        # print(response)
        #从结构化的数据中提取各种对应的元素
        zf = FindhouseItem()
        title_list = response.xpath("/html/body/div[5]/ul[2]/li/div/div[1]/a/text()").extract()
        price_list = response.xpath("/html/body/div[5]/ul[2]/li/div/div[4]/div[1]/span[1]/text()").extract()
        for i,j in zip(title_list,price_list):
            zf['title'] = i
            zf['price'] = j
            #scrapy框架对含有yield的parse()方法的调用是以迭代的是进行的
            #yield中断访问，不用重新开始执行
            yield zf
