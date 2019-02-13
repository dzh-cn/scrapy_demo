# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import pymysql


class DoubanMoviePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect("localhost", "test", "test", "test")
        self.cursor = self.connect.cursor()
        self.sql = """insert into douban_movie(name,name_desc,stars,rating,rater_count) value (%s,%s,%s,%s,%s) on duplicate key update name=(name)"""


    # def process_item(self, item, spider):
    #     for i in range(0, len(item['name_desc'])):
    #         self.cursor.execute(self.sql, (item['name'][i*2], item['name_desc'], item['stars'], item['rating'], item['rater_count']))
    #     self.connect.commit()
    #     return item


    def process_item(self, item, spider):
        # self.cursor.execute(self.sql, (item['name'], item['name_desc'], item['stars'], item['rating'], item['rater_count']))
        # self.connect.commit()
        return item