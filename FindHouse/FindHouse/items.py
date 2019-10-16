# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#Items主要目标是从非结构化来源提取结构化数据，scrapy爬虫可以将提取的数据作为python语句返回
import scrapy

class FindhouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Field对象用于为每个字段指定元数据，Field用于声明项目的对象不会被分配为类属性。
    #可以通过Item.fields属性访问它们。
    title = scrapy.Field()
    price = scrapy.Field()