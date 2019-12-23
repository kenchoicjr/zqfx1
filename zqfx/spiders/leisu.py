# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import datetime
import time
from zqfx.items import *
from scrapy import cmdline
# from zqfx.spiders.analysis import *
from zqfx.selenium2 import HsxyCasUtil
# from fake_useragent import UserAgent
from selenium import webdriver
from scrapy.http import HtmlResponse
import json


class LeisuSpider(scrapy.Spider):
    with open("H:\zqfx1\zqfx\cookies.txt", "r")as f:
        cookies = f.read()
        cookies = json.loads(cookies)
    name = 'leisu'
    allowed_domains = ['leisu.com']
    # start_urls = []
    # url = "https://guide.leisu.com/swot-"
    # ua = UserAgent()
    print("-----------cookies-----------------" + str(cookies))
    headers = {
        "Host": "guide.leisu.com",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": " 1",
        "cookies":cookies
        }#"User-Agent": ua.random

    # response = requests.get(url, headers=headers)
    # html_str = response.content.decode()
    # _element = etree.HTML(html_str)
    # h = HsxyCasUtil()
    # list = h.get_list()
    # for i in list:
    #     start_urls.append(url + i)
    # print(start_urls)
    # start_urls = [
    #     "http://www.fox008.com/analysis/listV3?matchDate=" + datetime.datetime.strftime(datetime.datetime.now(),
    #
    def __init__(self, category=None, *args, **kwargs):
        super(LeisuSpider, self).__init__(*args, **kwargs)
        start_urls = []
        url = "https://guide.leisu.com/swot-"
        h = HsxyCasUtil()
        self.list = h.get_list()
        for self.i in self.list:
            # self.category = self.i
            # print(i.split("-")[0])
            self.start_urls.append(
                url + self.i.split("-")[0])  # self.start_urls = ['http://www.example.com/categories/%s' % category]

    def parse(self, response):
        time.sleep(1)
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                   options=options)

        driver.get(response.url)
        cookie = {}
        for i in driver.get_cookies():
            cookie[i["name"]] = i["value"]
        with open("H:\zqfx1\zqfx\cookies.txt", "w") as f:
            f.write(json.dumps(cookie))
        driver.implicitly_wait(2)
        with open("H:\zqfx1\zqfx\cookies.txt", "r")as f:
            cookies = f.read()
            cookies = json.loads(cookies)
        driver.implicitly_wait(2)
        session = requests.session()
        html = session.get(response.url, cookies=cookies)
        response_selenium = html.text  # 响应内容
        response = HtmlResponse(url=driver.current_url, body=response_selenium, encoding='utf-8')
        driver.quit()
        # print("------------------------------", response.text, "---------------------------")
        # print(self.list)
        # print()
        item = LeisuItem()

        for j in self.list:
            if response.url[-7:] == j.split("-")[0]:
                item['cc'] = j.split("-")[1]
                break

        date = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
        if len(response.xpath("//span[@class='clearfix-row']/text()")) == 4:
            team1 = response.xpath("//span[@class='clearfix-row']/text()")[0].extract()
            team2 = response.xpath("//span[@class='clearfix-row']/text()")[1].extract()
        elif len(response.xpath("//span[@class='clearfix-row']/text()")) == 5:
            team1 = response.xpath("//span[@class='clearfix-row']/text()")[0].extract()
            team2 = response.xpath("//span[@class='clearfix-row']/text()")[2].extract()
        win = response.xpath("//span[@class='txt']/text()")[0].extract()
        lose = response.xpath("//span[@class='txt']/text()")[1].extract()
        lsjf_left = response.xpath("//span[@class='num1']/text()")[0].extract() + \
                    response.xpath("//span[@class='float-left']/text()")[0].extract() + \
                    response.xpath("//span[@class='float-left']/span/text()")[0].extract() + \
                    response.xpath("//span[@class='float-left']/text()")[1].extract() + \
                    response.xpath("//span[@class='float-left']/span/text()")[1].extract() + \
                    response.xpath("//span[@class='float-left']/text()")[2].extract() + \
                    response.xpath("//span[@class='float-left']/span/text()")[2].extract()
        lsjf_right = response.xpath("//span[@class='num2']/text()")[0].extract() + \
                     response.xpath("//span[@class='float-right']/text()")[0].extract() + \
                     response.xpath("//span[@class='float-right']/span/text()")[0].extract() + \
                     response.xpath("//span[@class='float-right']/text()")[1].extract() + \
                     response.xpath("//span[@class='float-right']/span/text()")[1].extract() + \
                     response.xpath("//span[@class='float-right']/text()")[2].extract() + \
                     response.xpath("//span[@class='float-right']/span/text()")[2].extract()
        jqzj_left = response.xpath("//span[@class='num1']/text()")[1].extract() + \
                    response.xpath("//span[@class='float-left']/text()")[3].extract() + \
                    response.xpath("//span[@class='float-left']/span/text()")[3].extract() + \
                    response.xpath("//span[@class='float-left']/text()")[4].extract() + \
                    response.xpath("//span[@class='float-left']/span/text()")[4].extract() + \
                    response.xpath("//span[@class='float-left']/text()")[5].extract() + \
                    response.xpath("//span[@class='float-left']/span/text()")[5].extract()
        jqzj_right = response.xpath("//span[@class='num2']/text()")[1].extract() + \
                     response.xpath("//span[@class='float-right']/text()")[3].extract() + \
                     response.xpath("//span[@class='float-right']/span/text()")[3].extract() + \
                     response.xpath("//span[@class='float-right']/text()")[4].extract() + \
                     response.xpath("//span[@class='float-right']/span/text()")[4].extract() + \
                     response.xpath("//span[@class='float-right']/text()")[5].extract() + \
                     response.xpath("//span[@class='float-right']/span/text()")[5].extract()
        remarks = response.xpath("//td[@class='w-310']/span/text()")[0].extract() + "-" + \
                  response.xpath("//span[@class='f-s-38']/text()")[0].extract() + "-" + \
                  response.xpath("//span[@class='f-s-38']/text()")[1].extract() + "-" + \
                  response.xpath("//span[@class='f-s-38']/text()")[2].extract()
        item['information'] = ' '.join(response.xpath("//div[@id='information']//text()").extract())
        item['date'] = date
        item['url'] = response.url
        item['team1'] = team1
        item['lose'] = lose
        item['win'] = win
        item['team2'] = team2
        item['lsjf_left'] = lsjf_left
        item['lsjf_right'] = lsjf_right
        item['jqzj_left'] = jqzj_left
        item['jqzj_right'] = jqzj_right
        item['remarks'] = remarks
        yield item  # cmdline.execute("scrapy crawl live500".split())  # item['date'] = date  # print(date,team1,win,team2,lose,lsjf_left,lsjf_right,jqzj_left,jqzj_right,remarks)  # for l in list:  #     print(l.xpath("./text()").extract())  # print(l.xpath("./text()")[2].extract())  # for i in list:  #     item = ZqfxItem()  #     item['date'] = response.url[-8:]  #     item['cc'] = i.xpath(".//div[@class='fxs_1_01']/em/text()")[0].extract()  #     item['fxs_leauge'] = i.xpath(".//div[@class='fxs_1_01']/div[@class='fxs_leauge']/text()")[0].extract()  #     item['fxs_leauge_name0'] = i.xpath(".//div[@class='fxs_1_02']/div[@class='fxs_leauge_name']/div/text()")[  #         0].extract()  #     item['fxs_leauge_name1'] = i.xpath(".//div[@class='fxs_1_06']/div[@class='fxs_leauge_name']/div/text()")[  #         0].extract()  #     item['fxs_2_02_c01'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c01']/text()")[0].extract()  #     item['fxs_2_02_c03'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c03']/text()")[0].extract()  #     item['fxs_2_03_gailus1'] = i.xpath(".//div[@class='fxs_2_03']//div[@class='fxs_2_03_gailus1']/text()")[  #         0].extract()  #     item['predictc'] = i.xpath(".//div[@class='fxs_2_03']//div[@class='fxs_2_03_gailus']/text()")[0].extract()  #     item['fxs_2_02_c01y'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c01']/text()")[1].extract()  #     item['fxs_2_02_c01yp'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c01']/span/text()")[  #         0].extract()  #     item['fxs_2_02_c01yt'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c03']/text()")[1].extract()  #     item['fxs_2_02_c01yg'] = i.xpath(".//div[@class='fxs_2_03']//div[@class='fxs_2_03_gailus']/text()")[  #         1].extract()  #     # print(fxs_2_02_c03, "*************", fxs_2_02_c01yt)  #     # if fxs_2_02_c03.find(fxs_2_02_c01yt) > -1 and int(fxs_2_02_c01yg) > 53:#and int(fxs_2_02_c01yg) > 53  #     #     print(cc, fxs_leauge, fxs_leauge_name0, fxs_leauge_name1, fxs_2_02_c01, fxs_2_02_c03, fxs_2_03_gailus1,  #     #           predictc, fxs_2_02_c01y, fxs_2_02_c01yp, fxs_2_02_c01yt, fxs_2_02_c01yg)  #     # # print(date,cc, fxs_leauge, fxs_leauge_name0, fxs_leauge_name1, fxs_2_02_c01, fxs_2_02_c03, fxs_2_03_gailus1,  #     #       predictc, fxs_2_02_c01y, fxs_2_02_c01yp, fxs_2_02_c01yt, fxs_2_02_c01yg)  #     cl = i.xpath(".//div[@class='fxs_2_01']/a/@href")[0].extract().split("/")[-1]  #     cl = "http://www.fox008.com/analysis/tips/" + cl  #     # print(cl)  #     yield scrapy.Request(cl, callback=self.parse_item)  #     yield item  #  # cmdline.execute("scrapy crawl live500".split())

    def parse_item(self, response):
        print(response.url)
        if response.xpath("//div[@class='wrong_bg_taikong']") is not None:
            item = AnalysisItem()
            item["date"] = response.url.split("/")[5].split(".")[0][:8]
            item["cc"] = response.url.split("/")[5].split(".")[0][8:11]
            left = response.xpath("//div[@id='capacityV1']//td[@align='left']/text()")[0].extract()
            right = response.xpath("//div[@id='capacityV1']//td[@align='right']/text()")[0].extract()
            item["wjxs"] = (left + " 往绩系数 " + right)
            left_1 = response.xpath(
                "//div[@class='fx_qb_left350'][1]/div[contains(@class,'fx_qb_list')]/p/text()").extract()
            left_2 = response.xpath(
                "//div[@class='fx_qb_left350'][2]/div[contains(@class,'fx_qb_list')]/p/text()").extract()
            left_3 = response.xpath(
                "//div[@class='fx_qb_left350'][3]/div[contains(@class,'fx_qb_list')]/p/text()").extract()
            right_1 = response.xpath(
                "//div[@class='fx_qb_rig350'][1]/div[contains(@class,'fx_qb_list')]/p/text()").extract()
            right_2 = response.xpath(
                "//div[@class='fx_qb_rig350'][2]/div[contains(@class,'fx_qb_list')]/p/text()").extract()
            right_3 = response.xpath(
                "//div[@class='fx_qb_rig350'][3]/div[contains(@class,'fx_qb_list')]/p/text()").extract()

            item["slfx_left"] = str(''.join(left_1))
            item["slfx_right"] = str(''.join(right_1))
            item["sjfx_left"] = str(''.join(left_2))
            item["sjfx_rigft"] = str(''.join(right_2))
            item["wjjk_left"] = str(''.join(left_3))
            item["wjjk_rigft"] = str(''.join(right_3))

            data1 = response.xpath("//div[@class='fx_qb_m300']/table[1]//tr/td[@align='left']/span/text()").extract()
            data2 = response.xpath("//div[@class='fx_qb_m300']/table[1]//tr/td[@align='center']/span/text()").extract()
            data3 = response.xpath("//div[@class='fx_qb_m300']/table[1]//tr/td[@align='right']/span/text()").extract()

            data4 = response.xpath("//div[@class='fx_qb_m300']/table[3]//tr/td[@align='left']/span/text()").extract()
            data5 = response.xpath("//div[@class='fx_qb_m300']/table[3]//tr/td[@align='center']/span/text()").extract()
            data6 = response.xpath("//div[@class='fx_qb_m300']/table[3]//tr/td[@align='right']/span/text()").extract()

            item["op"] = str(''.join(data1) + " " + ''.join(data2) + " " + ''.join(data3))
            item["yp"] = str(''.join(data4) + " " + ''.join(data5) + " " + ''.join(data6))

            data7 = response.xpath(
                "//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/div/span/text()").extract()
            data8 = response.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/span/text()").extract()
            data8_1 = response.xpath(
                "//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/span/span/text()").extract()
            data9 = response.xpath(
                "//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/div/span/text()").extract()
            data10 = response.xpath(
                "//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/span/text()").extract()
            data10_1 = response.xpath(
                "//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/span/span/text()").extract()
            data11 = response.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='center'][1]/text()").extract()

            item["dzwj"] = str(''.join(data7[:6]) + " " + ''.join(data8[:2]) + " " + data11[0] + " " + ''.join(
                data9[:6]) + " " + ''.join(data10[:2]))
            item["_10cjk"] = str(
                ''.join(data7[6:12]) + " " + ''.join(data8[2:3]) + data8_1[0] + ''.join(data8[3:5]) + " " + data11[
                    1] + " " + ''.join(data9[6:12]) + " " + ''.join(data10[2:3]) + data10_1[0] + ''.join(data10[3:5]))
            item["pmxd"] = str(''.join(data7[12:18]) + " " + ''.join(data8[5:7]) + " " + data11[2] + " " + ''.join(
                data9[12:18]) + " " + ''.join(data10[5:7]))
            # print(item)
            yield (item)
