# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import datetime
from zqfx.items import *
from scrapy import cmdline


# from zqfx.spiders.analysis import *


class Fox008Spider(scrapy.Spider):
    name = 'fox008'
    allowed_domains = ['www.fox008.com']
    start_urls = []
    url = "http://www.fox008.com/analysis/listV3"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    response = requests.get(url, headers=headers)
    html_str = response.content.decode()
    _element = etree.HTML(html_str)
    list = _element.xpath('//select[@id="matchSelect"]/option/@value')
    for i in list:
        start_urls.append(url + "?matchDate=" + i)
    # print(start_urls)
    start_urls = [
        "http://www.fox008.com/analysis/listV3?matchDate=" + datetime.datetime.strftime(datetime.datetime.now(),
                                                                                        '%Y%m%d')]

    def parse(self, response):

        # print(datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d'))

        # print(response.url[-8:])
        list = response.xpath('//div[@sti]')
        for i in list:
            item = ZqfxItem()

            flag = (i.xpath(".//div[@class='fxs_1_10_nomatch']/text()")[0].extract())
            item['cc'] = i.xpath(".//div[@class='fxs_1_01']/em/text()")[0].extract()
            # print(item['cc'][-3:][0:1])
            if "未开赛" in flag and item['cc'][-3:][0:1] != '2':
                item['date'] = response.url[-8:]
                item['cc'] = i.xpath(".//div[@class='fxs_1_01']/em/text()")[0].extract()
                item['fxs_leauge'] = i.xpath(".//div[@class='fxs_1_01']/div[@class='fxs_leauge']/text()")[0].extract()
                item['fxs_leauge_name0'] = \
                    i.xpath(".//div[@class='fxs_1_02']/div[@class='fxs_leauge_name']/div/text()")[
                        0].extract()
                # print(item['fxs_leauge_name0'],i.xpath(".//div[@class='fxs_1_10_nomatch']/text()")[0].extract())
                item['fxs_leauge_name1'] = \
                    i.xpath(".//div[@class='fxs_1_06']/div[@class='fxs_leauge_name']/div/text()")[
                        0].extract()
                item['fxs_2_02_c01'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c01']/text()")[
                    0].extract()
                item['fxs_2_02_c03'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c03']/text()")[
                    0].extract()
                item['fxs_2_03_gailus1'] = i.xpath(".//div[@class='fxs_2_03']//div[@class='fxs_2_03_gailus1']/text()")[
                    0].extract()
                item['predictc'] = i.xpath(".//div[@class='fxs_2_03']//div[@class='fxs_2_03_gailus']/text()")[
                    0].extract()
                item['fxs_2_02_c01y'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c01']/text()")[
                    1].extract()
                item['fxs_2_02_c01yp'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c01']/span/text()")[
                    0].extract()
                item['fxs_2_02_c01yt'] = i.xpath(".//div[@class='fxs_2_02']/div[@class='fxs_2_02_c03']/text()")[
                    1].extract()
                item['fxs_2_02_c01yg'] = i.xpath(".//div[@class='fxs_2_03']//div[@class='fxs_2_03_gailus']/text()")[
                    1].extract()
                # print(fxs_2_02_c03, "*************", fxs_2_02_c01yt)
                # if fxs_2_02_c03.find(fxs_2_02_c01yt) > -1 and int(fxs_2_02_c01yg) > 53:#and int(fxs_2_02_c01yg) > 53
                #     print(cc, fxs_leauge, fxs_leauge_name0, fxs_leauge_name1, fxs_2_02_c01, fxs_2_02_c03, fxs_2_03_gailus1,
                #           predictc, fxs_2_02_c01y, fxs_2_02_c01yp, fxs_2_02_c01yt, fxs_2_02_c01yg)
                # # print(date,cc, fxs_leauge, fxs_leauge_name0, fxs_leauge_name1, fxs_2_02_c01, fxs_2_02_c03, fxs_2_03_gailus1,
                #       predictc, fxs_2_02_c01y, fxs_2_02_c01yp, fxs_2_02_c01yt, fxs_2_02_c01yg)
                cl = i.xpath(".//div[@class='fxs_2_01']/a/@href")[0].extract().split("/")[-1]
                cl = "http://www.fox008.com/analysis/tips/" + cl
                # print(cl)
                item['url']=cl
                yield scrapy.Request(cl, callback=self.parse_item)
                yield item  #

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

            item["dzwj"] = str(
                ''.join(data7[:6]) + " " + ''.join(data8[:2]) + " " + data11[0] + " " + ''.join(
                    data9[:6]) + " " + ''.join(
                    data10[:2]))
            item["_10cjk"] = str(
                ''.join(data7[6:12]) + " " + ''.join(data8[2:3]) + data8_1[0] + ''.join(data8[3:5]) + " " + data11[
                    1] + " " + ''.join(data9[6:12]) + " " + ''.join(data10[2:3]) + data10_1[0] + ''.join(data10[3:5]))
            item["pmxd"] = str(''.join(data7[12:18]) + " " + ''.join(data8[5:7]) + " " + data11[2] + " " + ''.join(
                data9[12:18]) + " " + ''.join(data10[5:7]))
            # print(item)
            yield (item)
