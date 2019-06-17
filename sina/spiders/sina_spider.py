import scrapy
from bs4 import BeautifulSoup
from sina.items import SinaItem
import re


class SinaSpider(scrapy.Spider):
    name = 'sina'
    start_urls = ['https://weibo.com/ttarticle/p/show?id=2309404381896548211358']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        title = soup.body.find(class_="main_editor").find(class_="title").string.strip()
        publish_time = soup.body.find(class_="main_editor").find(class_="time").string.strip()
        publish_time = re.sub(r'[\u4e00-\u9fa5]', '', publish_time).strip()
        read_num = soup.body.find(class_="main_editor").find(class_="W_fr").find(class_="num").string.strip()
        # 格式为阅读数：94577
        read_num = read_num[4:].strip()
        li_list = soup.body.find(class_="WB_feed").find(class_="WB_row_line").findAll('li')
        forward_num = li_list[0].find(class_="pos").span.string.strip()
        # 格式为转发 55
        forward_num = forward_num[2:].strip()
        comment_num = li_list[1].find(class_="pos").span.string.strip()
        # 格式为评论 6
        comment_num = comment_num[2:].strip()
        like_num = li_list[2].find(class_="pos").span.span.em.string.strip()
        item = SinaItem()
        item['title'] = title
        item['publish_time'] = publish_time
        item['read_num'] = read_num
        item['forward_num'] = forward_num
        item['comment_num'] = comment_num
        item['like_num'] = like_num
        yield item


