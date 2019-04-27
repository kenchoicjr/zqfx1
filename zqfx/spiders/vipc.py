# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from zqfx.items import *
from scrapy import cmdline


class VipcSpider(scrapy.Spider):
    name = 'vipc'
    allowed_domains = ['vipc.cn']
    start_urls = ["https://vipc.cn/jczq/singles"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self, response):
        # print(response.body.decode()) #v Mod_matchAnalysisCard.
        list = response.xpath("//a[@class='vMod_matchAnalysisCard']")
        date = response.xpath("//div[@class='vMatch3_nav_select']/select/option[@selected]/@value")[
            0].extract().replace("-", "")
        print(date)
        for i in list:
            flag = (i.xpath(".//div[@class='vMod_matchAnalysisCard_bottom']/p/text()").extract())
            # print(len(flag))
            if len(flag) == 0:
                print(i.xpath("./@title")[0].extract().split("：")[0].replace(" ", ""))
                print(i.xpath("./div[@class='vMod_matchAnalysisCard_ratio']/div[1]/text()")[0].extract())
                print(i.xpath("./div[@class='vMod_matchAnalysisCard_ratio']/div[3]/text()")[0].extract())
                print(i.xpath("./@href")[0].extract())
                print(i.xpath("./div[@class='vMod_matchAnalysisCard_bottom']/text()")[1].extract().strip())
