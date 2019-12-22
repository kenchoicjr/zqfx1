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
                url + self.i.split("*")[
                    0] + ".htm")  # self.start_urls = ['http://www.example.com/categories/%s' % category]

    def parse(self, response):

        # print(datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d'))
        # print(response.url[-11:-4])
        #
        # print(self.list)
        # print()
        time.sleep(0.8)
        item = Win007Item()
        item['url'] = response.url
        for j in self.list:
            if response.url[-11:-4] == j.split("*")[0]:
                item['cc'] = j.split("*")[2]
                item['date'] = j.split("*")[1].replace("-", "")
                # print(j.split("*")[2])
                item['match_time'] = j.split("*")[3]
                item['home_team'] = j.split("*")[4]
                item['guest_team'] = j.split("*")[5]
                item['h_odd'] = j.split("*")[6]
                item['pk'] = j.split("*")[7]
                item['g_odd'] = j.split("*")[8]
                item['full_result'] = j.split("*")[9]
                item['oddstr_281'] = "http://vip.win007.com/count/goalCount.aspx?t=5&sid={}&cid=281".format(j.split("*")[0])
                item['oddstr_115'] = "http://vip.win007.com/count/goalCount.aspx?t=5&sid={}&cid=115".format(j.split("*")[0])
                item['oddstr_82'] = "http://vip.win007.com/count/goalCount.aspx?t=5&sid={}&cid=158".format(j.split("*")[0])
                item['odds_3'] = "http://vip.win007.com/count/goalCount.aspx?t=1&sid={}&cid=3&l=2".format(j.split("*")[0])
                item['odds_8'] = "http://vip.win007.com/count/goalCount.aspx?t=1&sid={}&cid=8&l=2".format(j.split("*")[0])
                item['odds_14'] = "http://vip.win007.com/count/goalCount.aspx?t=1&sid={}&cid=14&l=2".format(j.split("*")[0])
                break

        # win = response.xpath("//span[@class='txt']/text()")[0].extract()
        mar_right601 = response.xpath("//div[@id='porlet_25']//font[@color='#6666ff']/text()")[0].extract()

        detail = response.xpath("//*[@id='porlet_25']//td[@bgcolor='#ffffff']/text()")[3].extract()
        match = response.xpath("//*[@id='porlet_25']//td[@bgcolor='#ffffff']/text()")[2].extract()
        # print(match)
        team1 = response.xpath("//*[@id='porlet_24']//tr[@class='red_t1']//b/text()")[0].extract()
        team2 = response.xpath("//*[@id='porlet_24']//tr[@class='blue_t1']//b/text()")[0].extract()
        mar_right1 = response.xpath("//*[@id='porlet_22']//td[@class='red16px']/text()")[0].extract()
        mar_right2 = response.xpath("//*[@id='porlet_22']//td[@class='red16px']/text()")[1].extract()
        mar_right3 = response.xpath("//*[@id='porlet_22']//td[@class='red16px']/text()")[2].extract()
        mar_right4 = response.xpath("//*[@id='porlet_22']//td[@class='red16px']/text()")[3].extract()
        mar_right5 = response.xpath("//*[@id='porlet_22']//td[@class='red16px']/text()")[4].extract()
        mar_right6 = response.xpath("//*[@id='porlet_22']//td[@class='red16px']/text()")[5].extract()
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
        item['mar_right1'] = mar_right1
        item['mar_right2'] = mar_right2
        item['mar_right3'] = mar_right3
        item['mar_right4'] = mar_right4
        item['mar_right5'] = mar_right5
        item['mar_right6'] = mar_right6
        item['detail'] = detail
        item['asian_odds_url'] = response.xpath("//*[@id='odds_menu']/li[3]/a/@href")[0].extract()
        item['oddslist_url'] = response.xpath("//*[@id='odds_menu']/li[5]/a/@href")[0].extract()
        # print(item['asian_odds_url'], item['oddslist_url'])
        url = item['oddslist_url']
        yield scrapy.Request(item['oddstr_281'], meta={'item': item}, callback=self.parse_item1, dont_filter=True)


    def parse_item1(self, response):
        time.sleep(2)
        item = response.meta['item']
        # print(response.body)/html/body/table[2]/tbody/tr[4]/td[5]/a
        oddstr_f_t = response.xpath("/html/body/table[2]/tbody/tr[4]/td[5]/a/text()")[0].extract()
        if oddstr_f_t=='0':
            oddstr_f_t='1'
        oddstr_f_h = response.xpath("/html/body/table[2]/tbody/tr[4]/td[6]/a/text()")[0].extract()
        oddstr_f_p = response.xpath("/html/body/table[2]/tbody/tr[4]/td[7]/a/text()")[0].extract()
        oddstr_f_g = response.xpath("/html/body/table[2]/tbody/tr[4]/td[8]/a/text()")[0].extract()
        # float('%.2f' % int(oddstr_f_p) / int(oddstr_f_t) * 100)
        item['oddstr_281_f_result'] = oddstr_f_t + "*" + str(
            float('%.2f' % (int(oddstr_f_h) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_p) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_g) / int(oddstr_f_t) * 100)))

        oddstr_l_t = response.xpath("/html/body/table[2]/tbody/tr[5]/td[5]/a/text()")[0].extract()
        if oddstr_l_t=='0':
            oddstr_l_t='1'
        oddstr_l_h = response.xpath("/html/body/table[2]/tbody/tr[5]/td[6]/a/text()")[0].extract()
        oddstr_l_p = response.xpath("/html/body/table[2]/tbody/tr[5]/td[7]/a/text()")[0].extract()
        oddstr_l_g = response.xpath("/html/body/table[2]/tbody/tr[5]/td[8]/a/text()")[0].extract()
        item['oddstr_281_l_result'] = oddstr_l_t + "*" + str(
            float('%.2f' % (int(oddstr_l_h) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_p) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_g) / int(oddstr_l_t) * 100)))
        # print(item['oddstr_281_f_result'],item['oddstr_281_l_result'])
        # print(item)
        yield scrapy.Request(item['oddstr_115'], meta={'item': item}, callback=self.parse_item4, dont_filter=True)

    def parse_item4(self, response):
        time.sleep(2)
        item = response.meta['item']
        oddstr_f_t = response.xpath("/html/body/table[2]/tbody/tr[4]/td[5]/a/text()")[0].extract()
        if oddstr_f_t=='0':
            oddstr_f_t='1'
        oddstr_f_h = response.xpath("/html/body/table[2]/tbody/tr[4]/td[6]/a/text()")[0].extract()
        oddstr_f_p = response.xpath("/html/body/table[2]/tbody/tr[4]/td[7]/a/text()")[0].extract()
        oddstr_f_g = response.xpath("/html/body/table[2]/tbody/tr[4]/td[8]/a/text()")[0].extract()
        item['oddstr_115_f_result'] = oddstr_f_t + "*" + str(
            float('%.2f' % (int(oddstr_f_h) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_p) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_g) / int(oddstr_f_t) * 100)))

        oddstr_l_t = response.xpath("/html/body/table[2]/tbody/tr[5]/td[5]/a/text()")[0].extract()
        if oddstr_l_t=='0':
            oddstr_l_t='1'
        oddstr_l_h = response.xpath("/html/body/table[2]/tbody/tr[5]/td[6]/a/text()")[0].extract()
        oddstr_l_p = response.xpath("/html/body/table[2]/tbody/tr[5]/td[7]/a/text()")[0].extract()
        oddstr_l_g = response.xpath("/html/body/table[2]/tbody/tr[5]/td[8]/a/text()")[0].extract()
        item['oddstr_115_l_result'] = oddstr_l_t + "*" + str(
            float('%.2f' % (int(oddstr_l_h) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_p) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_g) / int(oddstr_l_t) * 100)))
        yield scrapy.Request(item['oddstr_82'], meta={'item': item}, callback=self.parse_item5, dont_filter=True)

    def parse_item5(self, response):
        time.sleep(2)
        item = response.meta['item']
        oddstr_f_t = response.xpath("/html/body/table[2]/tbody/tr[4]/td[5]/a/text()")[0].extract()
        if oddstr_f_t=='0':
            oddstr_f_t='1'
        oddstr_f_h = response.xpath("/html/body/table[2]/tbody/tr[4]/td[6]/a/text()")[0].extract()
        oddstr_f_p = response.xpath("/html/body/table[2]/tbody/tr[4]/td[7]/a/text()")[0].extract()
        oddstr_f_g = response.xpath("/html/body/table[2]/tbody/tr[4]/td[8]/a/text()")[0].extract()
        item['oddstr_82_f_result'] = oddstr_f_t + "*" + str(
            float('%.2f' % (int(oddstr_f_h) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_p) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_g) / int(oddstr_f_t) * 100)))

        oddstr_l_t = response.xpath("/html/body/table[2]/tbody/tr[5]/td[5]/a/text()")[0].extract()
        if oddstr_l_t=='0':
            oddstr_l_t='1'
        oddstr_l_h = response.xpath("/html/body/table[2]/tbody/tr[5]/td[6]/a/text()")[0].extract()
        oddstr_l_p = response.xpath("/html/body/table[2]/tbody/tr[5]/td[7]/a/text()")[0].extract()
        oddstr_l_g = response.xpath("/html/body/table[2]/tbody/tr[5]/td[8]/a/text()")[0].extract()
        item['oddstr_82_l_result'] = oddstr_l_t + "*" + str(
            float('%.2f' % (int(oddstr_l_h) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_p) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_g) / int(oddstr_l_t) * 100)))
        # print(item)
        yield scrapy.Request(item['odds_3'], meta={'item': item}, callback=self.parse_item6, dont_filter=True)

    def parse_item6(self, response):
        time.sleep(2)
        item = response.meta['item']
        oddstr_f_t = response.xpath("/html/body/table[2]/tbody/tr[4]/td[5]/a/text()")[0].extract()
        if oddstr_f_t=='0':
            oddstr_f_t='1'
        oddstr_f_h = response.xpath("/html/body/table[2]/tbody/tr[4]/td[6]/a/text()")[0].extract()
        oddstr_f_p = response.xpath("/html/body/table[2]/tbody/tr[4]/td[7]/a/text()")[0].extract()
        oddstr_f_g = response.xpath("/html/body/table[2]/tbody/tr[4]/td[8]/a/text()")[0].extract()
        item['odds_3_f_result'] = oddstr_f_t + "*" + str(
            float('%.2f' % (int(oddstr_f_h) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_p) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_g) / int(oddstr_f_t) * 100)))

        oddstr_l_t = response.xpath("/html/body/table[2]/tbody/tr[5]/td[5]/a/text()")[0].extract()
        if oddstr_l_t=='0':
            oddstr_l_t='1'
        oddstr_l_h = response.xpath("/html/body/table[2]/tbody/tr[5]/td[6]/a/text()")[0].extract()
        oddstr_l_p = response.xpath("/html/body/table[2]/tbody/tr[5]/td[7]/a/text()")[0].extract()
        oddstr_l_g = response.xpath("/html/body/table[2]/tbody/tr[5]/td[8]/a/text()")[0].extract()
        item['odds_3_l_result'] = oddstr_l_t + "*" + str(
            float('%.2f' % (int(oddstr_l_h) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_p) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_g) / int(oddstr_l_t) * 100)))
        yield scrapy.Request(item['odds_8'], meta={'item': item}, callback=self.parse_item7, dont_filter=True)

    def parse_item7(self, response):
        time.sleep(2)
        item = response.meta['item']
        oddstr_f_t = response.xpath("/html/body/table[2]/tbody/tr[4]/td[5]/a/text()")[0].extract()
        if oddstr_f_t=='0':
            oddstr_f_t='1'
        oddstr_f_h = response.xpath("/html/body/table[2]/tbody/tr[4]/td[6]/a/text()")[0].extract()
        oddstr_f_p = response.xpath("/html/body/table[2]/tbody/tr[4]/td[7]/a/text()")[0].extract()
        oddstr_f_g = response.xpath("/html/body/table[2]/tbody/tr[4]/td[8]/a/text()")[0].extract()
        item['odds_8_f_result'] = oddstr_f_t + "*" + str(
            float('%.2f' % (int(oddstr_f_h) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_p) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_g) / int(oddstr_f_t) * 100)))

        oddstr_l_t = response.xpath("/html/body/table[2]/tbody/tr[5]/td[5]/a/text()")[0].extract()
        if oddstr_l_t=='0':
            oddstr_l_t='1'
        oddstr_l_h = response.xpath("/html/body/table[2]/tbody/tr[5]/td[6]/a/text()")[0].extract()
        oddstr_l_p = response.xpath("/html/body/table[2]/tbody/tr[5]/td[7]/a/text()")[0].extract()
        oddstr_l_g = response.xpath("/html/body/table[2]/tbody/tr[5]/td[8]/a/text()")[0].extract()
        item['odds_8_l_result'] = oddstr_l_t + "*" + str(
            float('%.2f' % (int(oddstr_l_h) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_p) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_g) / int(oddstr_l_t) * 100)))
        yield scrapy.Request(item['odds_14'], meta={'item': item}, callback=self.parse_item8, dont_filter=True)

    def parse_item8(self, response):
        time.sleep(2)
        item = response.meta['item']
        oddstr_f_t = response.xpath("/html/body/table[2]/tbody/tr[4]/td[5]/a/text()")[0].extract()
        if oddstr_f_t=='0':
            oddstr_f_t='1'
        oddstr_f_h = response.xpath("/html/body/table[2]/tbody/tr[4]/td[6]/a/text()")[0].extract()
        oddstr_f_p = response.xpath("/html/body/table[2]/tbody/tr[4]/td[7]/a/text()")[0].extract()
        oddstr_f_g = response.xpath("/html/body/table[2]/tbody/tr[4]/td[8]/a/text()")[0].extract()
        item['odds_14_f_result'] = oddstr_f_t + "*" + str(
            float('%.2f' % (int(oddstr_f_h) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_p) / int(oddstr_f_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_f_g) / int(oddstr_f_t) * 100)))

        oddstr_l_t = response.xpath("/html/body/table[2]/tbody/tr[5]/td[5]/a/text()")[0].extract()
        if oddstr_l_t=='0':
            oddstr_l_t='1'
        oddstr_l_h = response.xpath("/html/body/table[2]/tbody/tr[5]/td[6]/a/text()")[0].extract()
        oddstr_l_p = response.xpath("/html/body/table[2]/tbody/tr[5]/td[7]/a/text()")[0].extract()
        oddstr_l_g = response.xpath("/html/body/table[2]/tbody/tr[5]/td[8]/a/text()")[0].extract()
        item['odds_14_l_result'] = oddstr_l_t + "*" + str(
            float('%.2f' % (int(oddstr_l_h) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_p) / int(oddstr_l_t) * 100))) + "*" + str(
            float('%.2f' % (int(oddstr_l_g) / int(oddstr_l_t) * 100)))
        print(item)
        yield item

