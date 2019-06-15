# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from sina.util.db import DBConnection


class SinaPipeline(object):
    def process_item(self, item, spider):
        sql = "INSERT INTO `article` ( `title`, `publish_time`, `read_num`, `forward_num`, `comment_num`, `like_num`, `created_time`, `updated_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (item['title'], item['publish_time'], item['read_num'], item['forward_num'],
                  item['comment_num'], item['like_num'], int(time.time()), int(time.time()))
        conn = DBConnection()
        conn.execute(sql, params)
        return item
