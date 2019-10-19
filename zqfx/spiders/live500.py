# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from zqfx.items import *
from scrapy import cmdline


class Live500Spider(scrapy.Spider):
    name = 'live500'
    allowed_domains = ['500.com']
    start_urls = [
        'http://live.500.com/?e=' + datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=-1),
                                                               '%Y-%m-%d'),
        'http://live.500.com/?e=' + datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=-2),
                                                               '%Y-%m-%d'),
        'http://live.500.com/?e=' + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')]

    def parse(self, response):
        # print(response.url[-10:].replace("-", ""))

        R_json = response.xpath("//script[@type='text/javascript'][5]/text()").extract()
        print("++++++++++++++++++++++++++++++++++++", R_json)
        list = str(R_json)
        # print(response.body.decode("GBK"))http://live.500.com/?e=2019-03-31
        str1 = list.replace('var liveOddsList=', '')
        # print(eval(str1))
        list2 = eval(str1)
        # data = json.loads(list2[0])
        json1 = (json.loads(list2[0].replace(";", "")))
        # print(json1)
        lists = response.xpath("//table[@id='table_match']//td[@class=''][1]")
        for l in lists:
            item = ZqfxItem1()
            # print(l.xpath("./text()")[0].extract(), l.xpath("./input/@value")[0].extract())
            fid = l.xpath("./input/@value")[0].extract()
            # print(json1[fid]["sp"])
            # print(l.xpath("../td[@class='red'][2]/text()")[0].extract())
            item["date"] = response.url[-10:].replace("-", "")
            item["cc"] = l.xpath("./text()")[0].extract()
            item["result"] = l.xpath("../td[@class='red'][2]/text()")[0].extract()
            if json1[fid].get("sp") is None:
                item["w"] = "0"
                item["p"] = "0"
                item["l"] = "0"
            else:
                item["w"] = json1[fid].get("sp")[0] if json1[fid].get("sp")[0] is not None else "0"
                item["p"] = json1[fid].get("sp")[1] if json1[fid].get("sp")[1] is not None else "0"
                item["l"] = json1[fid].get("sp")[2] if json1[fid].get("sp")[2] is not None else "0"
            # print(item["bf_op"])
            cl = "https:" + (l.xpath("../td[@class='td_warn']//a[@target='_blank'][1]/@href")[0].extract())
            yield scrapy.Request(cl, meta={'item': item},
                                 callback=self.parse_item)  # yield item  # team1 = (l.xpath("../td[@class='p_lr01' and @align='right']/a/text()")[0].extract())  # team2 = (l.xpath("../td[@class='p_lr01' and @align='left']/a/text()")[0].extract())  # print(team1, team2)

        # cmdline.execute("scrapy crawl fox008".split())  # cmdline.execute("scrapy crawl analysis".split())

    def parse_item(self, response):
        # print(response.url)
        item = response.meta['item']
        # print(item)
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
