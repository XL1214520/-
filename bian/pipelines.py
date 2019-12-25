# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib import request

class BianPipeline(object):
    def process_item(self, item, spider):
        curPath = "G:/壁纸"
        tempPath = str(item['classification_title'])
        targetPath = curPath + os.path.sep + tempPath
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        filename_path = "G:/壁纸" + os.path.sep + str(item['classification_title']) + os.path.sep + str(item["img_name"]) + '.jpg'
        request.urlretrieve(item['img_download'],filename_path)
        return item
