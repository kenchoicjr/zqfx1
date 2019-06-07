# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import datetime
from zqfx.items import *
from scrapy import cmdline
import json


# from zqfx.spiders.analysis import *


class SportterySpider(scrapy.Spider):
    name = 'sporttery'
    allowed_domains = ['sporttery.cn']
    start_urls = []
    url = "https://info.sporttery.cn/football/match_result.php?search_league=0&start_date=2019-05-04&end_date=" + datetime.datetime.strftime(
        datetime.datetime.now(), '%Y-%m-%d' + '&page={}')
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    response = requests.get(url, headers=headers)
    html_str = response.content.decode("GBK")
    _element = etree.HTML(html_str)

    pages = _element.xpath("//a[@title='尾页']/@href")[0]
    start = int((pages.find('?page=') + len('?page=')))
    end = int(pages.find('&'))
    # print(start, end)
    # print(pages[start:end])
    for i in range(1, int(pages[start:end]) + 1):
        start_urls.append(url.format(i))

    def parse(self, response):
        # print(response.url)
        list = response.xpath('//div[@class="match_list"]//tr')
        for i in list:
            status = (i.xpath("./td[@width='86']/text()").extract())
            if len(status) > 0:
                if status[0] == "已完成":
                    item = SportteryItem()
                    item['date'] = (i.xpath("./td[@width='101']/text()")[0].extract()).replace("-", "")
                    item['cc'] = (i.xpath("./td[@width='104']/text()")[0].extract())[-3:]
                    item['league'] = (i.xpath("./td[@width='112']/text()")[0].extract())
                    item['zhu'] = (i.xpath("./td[@class='td_zk']//span[@class='zhu']/text()")[0].extract())
                    item['ke'] = (i.xpath("./td[@class='td_zk']//span[@class='ke']/text()")[0].extract())
                    item['half'] = (i.xpath("./td[@width='60']//span[@class='blue']/text()")[0].extract())
                    item['full'] = (i.xpath("./td[@width='60']//span[@class='u-org']/text()")[0].extract())
                    item['w'] = (i.xpath("./td[@width='55']//span/text()")[0].extract())
                    item['p'] = (i.xpath("./td[@width='55']//span/text()")[1].extract())
                    item['l'] = (i.xpath("./td[@width='55']//span/text()")[2].extract())
                    # item['result'] = "https:" + (i.xpath("./td[@class='u-detal']/a/@href")[0].extract())

                    sameIndex = int(i.xpath("./td[@class='u-detal']/a/@href")[1].extract().find("=")) + 1
                    item['sameIndex'] = i.xpath("./td[@class='u-detal']/a/@href")[1].extract()[sameIndex:]
                    item[
                        'result'] = "https://i.sporttery.cn/api/fb_match_info/get_pool_rs/?f_callback=pool_prcess&mid=" + item['sameIndex']

                    item['same'] = "https://info.sporttery.cn/football/search_odds.php?mid=" + item['sameIndex']
                    item['analysis'] = "https://i.sporttery.cn/api/fb_match_info/get_match_news_list?mid=" + item['sameIndex']
                    # print(date, cc, league, zhu, ke, half, full, w, p, l, result, analysis, same)
                    # print(item,same)
                    yield scrapy.Request(item['result'], meta={'item': item}, callback=self.parse_item)

    def parse_item(self, response):
        # print("*****************", response.url)
        item = response.meta['item']
        # print("*****************", item)
        # print(response.body.decode("GBK"))
        # yield (item)
        # 返回的是json数据
        # 转换为python中的字典
        rs = json.loads(response.text.replace(");", "").replace("pool_prcess(", ""), encoding="utf-8")
        # print(rs.get('result').get('odds_list').get('had').get('odds')[-1])
        # print(len(rs.get('result').get('odds_list').get('had').get('odds')))
        if rs.get('status').get('code') == 0:
            item['had_odds'] = (rs.get('result').get('pool_rs').get('had').get('odds'))
            item['hhad_odds'] = (rs.get('result').get('pool_rs').get('hhad').get('odds'))
            item['crs_odds'] = (rs.get('result').get('pool_rs').get('crs').get('odds'))
            item['ttg_odds'] = (rs.get('result').get('pool_rs').get('ttg').get('odds'))
            item['hafu_odds'] = (rs.get('result').get('pool_rs').get('hafu').get('odds'))
            item['had_prs_name'] = (rs.get('result').get('pool_rs').get('had').get('prs_name'))
            item['hhad_prs_name'] = (
                    "(" + rs.get('result').get('pool_rs').get('hhad').get('goalline') + ")" + rs.get('result').get(
                'pool_rs').get('hhad').get('prs_name'))
            item['crs_prs_name'] = (rs.get('result').get('pool_rs').get('crs').get('prs_name'))
            item['ttg_prs_name'] = (rs.get('result').get('pool_rs').get('ttg').get('prs_name'))
            item['hafu_prs_name'] = (rs.get('result').get('pool_rs').get('hafu').get('prs_name'))
            # print("*****************", item)
            h = rs.get('result').get('odds_list').get('had').get('odds')[-1].get('h')
            a = rs.get('result').get('odds_list').get('had').get('odds')[-1].get('a')
            d = rs.get('result').get('odds_list').get('had').get('odds')[-1].get('d')
            url = "https://i.sporttery.cn/api/fb_prize_odds/get_odds?f_call=get_odds&type=all&dan=0&h_odds={}&a_odds={}&d_odds={}".format(
                h, a, d)
            yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item1)  # print(url)  # pass

    def parse_item1(self, response):
        rs = json.loads(response.text.replace(")", "").replace("get_odds(", ""), encoding="utf-8")
        item = response.meta['item']
        total = int(len((rs.get('result'))))
        w_num = 0
        p_num = 0
        l_num = 0
        if total > 0:
            for i in rs.get('result'):
                list = i.get('final').split(':')
                if list[0] > list[1]:
                    w_num += 1
                elif list[0] < list[1]:
                    l_num += 1
                else:
                    p_num += 1

            list1 = [str(total), '{:.2%}'.format(w_num / total), '{:.2%}'.format(p_num / total),
                     '{:.2%}'.format(l_num / total)]
            item['same_result'] = ' '.join(list1)
        # print(item)
        yield scrapy.Request(item['analysis'], meta={'item': item}, callback=self.parse_item2)

    def parse_item2(self, response):
        item = response.meta['item']
        rs = json.loads(response.text, encoding="utf-8")
        if rs.get('status').get('code') == 0:
            for i in rs.get('result'):
                # print(i.get('adesc'))
                if (i.get('adesc').split(' ')[0][-3:]) == item['cc'] or len(rs.get('result')) == 1:
                    yield scrapy.Request(i.get('url'), meta={'item': item}, callback=self.parse_item3)  # pass
        else:
            item['detail'] = ''
            url = 'https://i.sporttery.cn/api/cm_match_analys/get_match_data?f_callback=getData&mid=' + str(
                item['sameIndex'])
            # print(url)
            yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item4)

    def parse_item3(self, response):
        item = response.meta['item']
        # print(response.body.decode("GBK"))
        item['detail'] = "".join(
            response.xpath('//div[@class="con"]')[0].xpath('string(.)').extract()[0].strip().split())
        # item['detail'] = "".join(
        #     response.xpath('//div[@class="con"]')[0].xpath('string(.)').extract()[0].strip().split())
        # print(detail)
        url = 'https://i.sporttery.cn/api/cm_match_analys/get_match_data?f_callback=getData&mid=' + str(
            item['sameIndex'])
        # print(url)
        yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item4)

    def parse_item4(self, response):
        item = response.meta['item']
        rs = json.loads(response.text.replace(");", "").replace("getData(", ""), encoding="utf-8")
        # print(rs)
        item['had_h_rate'] = rs.get('result').get('had_h_rate')
        item['had_d_rate'] = rs.get('result').get('had_d_rate')
        item['had_a_rate'] = rs.get('result').get('had_a_rate')
        url = 'https://i.sporttery.cn/api/fb_match_info/get_match_info?f_callback=getMatchInfo&mid=' + str(
            item['sameIndex'])
        # print("--"*100,url)
        yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item5)  # yield (item)

    def parse_item5(self, response):
        item = response.meta['item']
        # print("-1-" * 100, response.url)
        rs = json.loads(response.text.replace(");", "").replace("getMatchInfo(", ""), encoding="utf-8")
        time_cn = int(rs.get('result').get('time_cn').split(':')[0])
        if time_cn >= 0 and time_cn < 12:
            date_cn = rs.get('result').get('date_cn')
            str2date = datetime.datetime.strptime(date_cn, "%Y-%m-%d")
            pre_date = str2date + datetime.timedelta(days=-1)
            # print("*"*50,pre_date)
            # date = date_cn + datetime.timedelta(days=-1)
            item['date'] = datetime.datetime.strftime(pre_date, '%Y%m%d')  # item['date'] = date
        # print(item)
        yield (item)  # yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item4)
