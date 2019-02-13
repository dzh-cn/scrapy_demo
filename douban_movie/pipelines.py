# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import pymysql


class DoubanMoviePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect("172.25.4.218", "m_test", "jZetUn", "test")
        self.cursor = self.connect.cursor()
        self.sql = """insert into movie_top_250(url,number,name,time,director,scenario,starts,type,district,language,time_desc) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update name=(name)"""


    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['url'], item['number'], item['name'], item['time'], item['director'], item['scenario'], str(item['starts']), str(item['type']), item['district'], item['language'], str(item['time_desc'])))
        self.connect.commit()
        return item