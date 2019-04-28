# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from zqfx.items import *
from scrapy import cmdline
from selenium import webdriver


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
        # print(date)
        for i in list:
            item = VipcItem()
            item["date"] = date
            flag = (i.xpath(".//div[@class='vMod_matchAnalysisCard_bottom']/p/text()").extract())
            # print(len(flag))
            if len(flag) == 0:
                item["cc"] = (i.xpath("./@title")[0].extract().split("：")[0].replace(" ", ""))
                item["win"] = (i.xpath("./div[@class='vMod_matchAnalysisCard_ratio']/div[1]/text()")[0].extract())
                item["lose"] = (i.xpath("./div[@class='vMod_matchAnalysisCard_ratio']/div[3]/text()")[0].extract())
                # print(i.xpath("./@href")[0].extract())
                if (i.xpath("./div[@class='vMod_matchAnalysisCard_bottom']/text()")[1].extract().strip()).find("；")>0:
                    item["result"] = \
                        (i.xpath("./div[@class='vMod_matchAnalysisCard_bottom']/text()")[1].extract().strip()).split(
                            "；")[0]
                    item["bf"] = \
                        (i.xpath("./div[@class='vMod_matchAnalysisCard_bottom']/text()")[1].extract().strip()).split(
                            "；")[1]
                else:
                    item["result"] = i.xpath("./div[@class='vMod_matchAnalysisCard_bottom']/text()")[
                        1].extract().strip()
                    item["bf"] = "  "
                item["url"] = "https://vipc.cn" + i.xpath("./@href")[0].extract().replace("#", "#/")
                yield (item)  # yield item

    # def parse_item(self, response):  #     options = webdriver.FirefoxOptions()  # options.add_argument('-headless')  # driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe', options=options)  # driver.get(response.url)  # remarks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[5]/div/div[1]/div[3]/div/p[1]/text()')  # print(remarks)
