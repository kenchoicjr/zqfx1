# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import datetime
import time
from zqfx.items import *
from scrapy import cmdline
# from zqfx.spiders.analysis import *
from zqfx.selenium3 import HsxyCasUtil


class Win007Spider(scrapy.Spider):
    name = 'win007'
    allowed_domains = ['win007']
    # start_urls = []
    # url = "https://guide.leisu.com/swot-"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


    def __init__(self, category=None, *args, **kwargs):
        super(Win007Spider, self).__init__(*args, **kwargs)
        start_urls = []
        url = "http://zq.win007.com/analysis/"
        h = HsxyCasUtil()
        self.list = h.get_list()
        for self.i in self.list:
            # self.category = self.i
            # print(i.split("-")[0])
            self.start_urls.append(
                url + self.i.split("*")[0]+".htm")  # self.start_urls = ['http://www.example.com/categories/%s' % category]

    def parse(self, response):

        # print(datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d'))
        # print(response.url[-11:-4])
        #
        # print(self.list)
        # print()
        time.sleep(0.5)
        item = Win007Item()
        item['url'] = response.url
        for j in self.list:
            if response.url[-11:-4] == j.split("*")[0]:
                item['cc'] = j.split("*")[2]
                item['date'] = j.split("*")[1].replace("-","")
                # print(j.split("*")[2])
                break

        # win = response.xpath("//span[@class='txt']/text()")[0].extract()
        mar_right601 = response.xpath("//div[@id='porlet_25']//font[@color='#6666ff']/text()")[0].extract()

        detail = response.xpath("//*[@id='porlet_25']//td[@bgcolor='#ffffff']/text()")[3].extract()
        match = response.xpath("//*[@id='porlet_25']//td[@bgcolor='#ffffff']/text()")[2].extract()
        # print(match)
        team1 = response.xpath("//*[@id='porlet_24']//tr[@class='red_t1']//b/text()")[0].extract()
        team2 = response.xpath("//*[@id='porlet_24']//tr[@class='blue_t1']//b/text()")[0].extract()
        # print(team1, team2, mar_right601)
        if team1.find(mar_right601) != -1:
            mar_right60 = "主胜"
        elif team2.find(mar_right601) != -1:
            mar_right60 = "客胜"
        elif mar_right601 == "和局":
            mar_right60 = "平手"
        elif match.find(team1) != -1:
            mar_right60 = "客胜"
        elif match.find(team2) != -1:
            mar_right60 = "主胜"
        item['mar_right60'] = mar_right60
        item['detail'] = detail
        print(item)
        # yield item

