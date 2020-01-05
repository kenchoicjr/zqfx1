# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from zqfx.items import *
from scrapy import cmdline
from selenium import webdriver
from scrapy.http import HtmlResponse
from zqfx.myresponse import MyResponse


class VipcSpider(scrapy.Spider):
    name = 'vipc'
    allowed_domains = ['vipc.cn']
    start_urls = ["https://vipc.cn/jczq/singles/" + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')]
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self, response):
        # print(response.getStatusCode())
        # print(response.body.decode()) #v Mod_matchAnalysisCard.
        # options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        # driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
        #                            options=options)
        # driver.get(response.url)
        # print(driver.page_source)
        myResponse = MyResponse()
        response = myResponse.get_list(response.url)
        # driver.quit()
        myResponse.close_driver()
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
                item["home"] = (i.xpath(".//div[@class='team']/span/text()")[0].extract())
                item["guest"] = (i.xpath(".//div[@class='team']/span/text()")[1].extract())
                item["cc"] = (i.xpath("./@title")[0].extract().split("：")[0].replace(" ", ""))
                item["win"] = (i.xpath("./div[@class='vMod_matchAnalysisCard_ratio']/div[1]/text()")[0].extract())
                item["lose"] = (i.xpath("./div[@class='vMod_matchAnalysisCard_ratio']/div[3]/text()")[0].extract())
                # print(i.xpath("./@href")[0].extract())
                if (i.xpath("./div[@class='vMod_matchAnalysisCard_bottom']/text()")[1].extract().strip()).find("；") > 0:
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
                # print(item["url"][-13:-4])
                next_url = "https://vipc.cn/i/match/football/{}/old-data".format(item["url"][-13:-4])
                # print(next_url)
                yield scrapy.Request(next_url, meta={'item': item}, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        item = response.meta['item']
        # options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        # driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
        #                            options=options)
        # driver.get(response.url)
        # print(driver.page_source)
        # print(response.xpath("//div[@id='json']/text()")[0].extract())
        myResponse = MyResponse()
        response = myResponse.get_list(response.url)
        # response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
        # myResponse.close_driver()
        json_text = response.xpath("//div[@id='json']/text()")[0].extract()
        rs = json.loads(json_text)
        item['content'] = rs.get("content")
        item['matchId'] = rs.get("matchId")
        next_url = "https://vipc.cn/i/match/football/{}/sporttery".format(item['matchId'])
        yield scrapy.Request(next_url, meta={'item': item,"myResponse":myResponse}, callback=self.parse_item1,dont_filter=True)

    def parse_item1(self, response):
        item = response.meta['item']
        myResponse = response.meta['myResponse']
        # print("------------------*----------*-***********************---------------------------",type(myResponse))
        # options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        # driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
        #                            options=options)
        # driver.get(response.url)
        # print(driver.page_source)
        # response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
        # driver.quit()
        # myResponse = MyResponse()
        response = myResponse.get_list(response.url)
        # response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
        myResponse.close_driver()
        json_text = response.xpath("//div[@id='json']/text()")[0].extract()
        rs = json.loads(json_text)
        # print(rs.get("yk").get("suggest")[0])
        winRatio = rs.get("support").get("winRatio")
        drawRatio = rs.get("support").get("drawRatio")
        loseRatio = rs.get("support").get("loseRatio")
        winPer = rs.get("support").get("winPer")
        drawPer = rs.get("support").get("drawPer")
        losePer = rs.get("support").get("losePer")
        winNum = rs.get("support").get("winNum")
        drawNum = rs.get("support").get("drawNum")
        loseNum = rs.get("support").get("loseNum")
        bettingRatio = rs.get("yk").get("bettingRatio")
        item['ratio'] = (winRatio + "        " + drawRatio + "        " + loseRatio)
        item['num'] =( winPer + "(" + winNum + ")" + "  " + drawPer + "(" + drawNum + ")" + "  " + losePer + "(" + loseNum + ")" )
        item['suggest0'] = rs.get("yk").get("suggest")[0]
        item['letgoal'] =("让球 ({}) 胜平负".format(rs.get("odds").get("letGoal")))
        item['betting'] = bettingRatio[3] + "        " + bettingRatio[4] + "        " + bettingRatio[5]
        item['suggest1']= rs.get("yk").get("suggest")[1]
        # print(winRatio+"        "+drawRatio+"        "+loseRatio)
        # rs.get("support").get("drawRatio")
        # rs.get("support").get("loseRatio")
        # print(rs)
        yield (item)  # yield item
