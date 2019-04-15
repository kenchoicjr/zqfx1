# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from zqfx.items import *


class AnalysisSpider(scrapy.Spider):
    name = 'analysis'
    allowed_domains = ['www.fox008.com']
    base_url = "http://www.fox008.com/analysis/tips/" + datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    start_urls = []
    for i in range(1, 70):
        s = str(i).zfill(3)
        start_urls.append(base_url + s + ".html")

    def parse(self, response):
        # print(response.url[-10:].replace("-", ""))
        # print(response.url.split("/")[5].split(".")[0][:8])
        # print(response.xpath("//div[@class='wrong_bg_taikong']/text()")[0].extract())
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

            data7 = response.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/div/span/text()").extract()
            data8 = response.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/span/text()").extract()
            data8_1 = response.xpath(
                "//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/span/span/text()").extract()
            data9 = response.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/div/span/text()").extract()
            data10 = response.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/span/text()").extract()
            data10_1 = response.xpath(
                "//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/span/span/text()").extract()
            data11 = response.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='center'][1]/text()").extract()

            item["dzwj"] = str(
                ''.join(data7[:6]) + " " + ''.join(data8[:2]) + " " + data11[0] + " " + ''.join(data9[:6]) + " " + ''.join(
                    data10[:2]))
            item["_10cjk"] = str(
                ''.join(data7[6:12]) + " " + ''.join(data8[2:3]) + data8_1[0] + ''.join(data8[3:5]) + " " + data11[
                    1] + " " + ''.join(data9[6:12]) + " " + ''.join(data10[2:3]) + data10_1[0] + ''.join(data10[3:5]))
            item["pmxd"] = str(''.join(data7[12:18]) + " " + ''.join(data8[5:7]) + " " + data11[2] + " " + ''.join(
                data9[12:18]) + " " + ''.join(data10[5:7]))
            # print(item)
            yield (item)

        # print(item["bf_op"])  # yield item
