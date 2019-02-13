# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    time = scrapy.Field()
    director = scrapy.Field()
    scenario = scrapy.Field()
    starts = scrapy.Field()
    type = scrapy.Field()
    district = scrapy.Field()
    language = scrapy.Field()
    time_desc = scrapy.Field()
    pass