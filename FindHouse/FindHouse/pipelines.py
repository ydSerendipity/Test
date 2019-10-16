# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#sqlite是python自带的轻量级数据库
import sqlite3

#连接数据库，没有则创建
findhouse = sqlite3.connect("findhouse.sqlite")
create_table = 'create table findhouse (title varchar(512), price varchar(128))'
#创建表，有则声明已创建
try:
    findhouse.execute(create_table)
except sqlite3.OperationalError as e:
    print("yichuanjian")

class FindhousePipeline(object):

    #当爬虫被打开的时候调用这个方法
    def open_spider(self,spider):
        self.con = sqlite3.connect("findhouse.sqlite")
        self.con.text_factory=str
        self.cu = self.con.cursor()

    #爬虫爬取到数据存放到items之后，返回的items对象会触发pipelines对items对象的操作，它主要存放在piplines.py中
    def process_item(self, item, spider):
        insert_sql = "insert into findhouse (title,price) values('{}','{}')".format(item['title'],item['price'])
        self.cu.execute(insert_sql)
        self.con.commit()
        #我的数据库是坏的，用这个测试一下
        # con = 'title:' + str(item['title']) + 'price:' + str(item['price']) + '\n'
        # with open(r'F:\Pycharm\FindHouse\FindHouse\spiders\price.csv', 'a', encoding='utf-8') as f:
        #     f.write(con)
        return item

    #爬虫关闭调用
    def spider_close(self,spider):
        self.con.close()
