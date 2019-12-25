# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class BianItem(Item):
    # 图片分类
    classification_title = Field()
    # 图片名字
    img_name = Field()
    # 图片下载地址
    img_download = Field()
