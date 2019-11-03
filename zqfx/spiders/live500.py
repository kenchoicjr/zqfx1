# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from zqfx.items import *
from zqfx.selenium4 import HsxyCasUtil
from scrapy import cmdline


class Live500Spider(scrapy.Spider):
    name = 'live500'
    allowed_domains = ['500.com']

    def __init__(self, category=None, *args, **kwargs):
        super(Live500Spider, self).__init__(*args, **kwargs)
        start_urls = []

        h = HsxyCasUtil()
        self.list = h.get_list()
        for self.i in self.list:
            # self.category = self.i
            # print(i.split("-")[0])
            self.start_urls.append(
                self.i.split("*")[6])  # self.start_urls = ['http://www.example.com/categories/%s' % category]

    def parse(self, response):
        print(response.url)

        item = ZqfxItem1()

        for j in self.list:
            if response.url.find(j.split("*")[7]) > 0:
                item['date'] = j.split("*")[0].replace("-","")
                item['cc'] = j.split("*")[1]
                item['result'] = j.split("*")[5]
                item['w'] = j.split("*")[2]
                item['p'] = j.split("*")[3]
                item['l'] = j.split("*")[4]
                break

        # print(l.xpath("./text()")[0].extract(), l.xpath("./input/@value")[0].extract())
        try:
            mar_right601 = response.xpath("//span[@class='mar_right60']/font/text()")[0].extract()
        except Exception:
            item['mar_right60'] = " "
            item['detail'] = " "
        else:
            mar_right601 = response.xpath("//span[@class='mar_right60']/font/text()")[0].extract()
            detail = response.xpath("//td[@class='td_one td_no4']/text()")[0].extract()
            # item['mar_right60'] = mar_right60
            # item['detail'] = detail
            team1 = response.xpath("//div[@class='M_box recommend']//td[@class='td_one']/text()")[0].extract()
            team2 = response.xpath("//div[@class='M_box recommend']//td[@class='td_one']/text()")[1].extract()
            print(team1, team2, mar_right601)
            if team1.find(mar_right601) != -1:
                mar_right60 = "主胜"
            elif team2.find(mar_right601) != -1:
                mar_right60 = "客胜"
            elif mar_right601 == "和局":
                mar_right60 = "平手"
            item['mar_right60'] = mar_right60
            item['detail'] = detail
        yield item
