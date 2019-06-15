# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    title = scrapy.Field()
    publish_time = scrapy.Field()
    read_num = scrapy.Field()
    forward_num = scrapy.Field()
    comment_num = scrapy.Field()
    like_num = scrapy.Field()
