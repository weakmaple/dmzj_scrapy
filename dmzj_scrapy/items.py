# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmzjScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pic_urls是一话所有图片的链接
    #title该话的名字（第一话，第二话 之类的）
    #big_title指的是漫画的名字
    pic_urls = scrapy.Field()
    title = scrapy.Field()
    big_title = scrapy.Field()