# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import datetime
from zqfx.items import *
from scrapy import cmdline
import json


# from zqfx.spiders.analysis import *


class NowSpider(scrapy.Spider):
    name = 'now'
    allowed_domains = ['sporttery.cn']
    start_urls = ['https://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=hhad&poolcode[]=had']


    def parse(self, response):
        rs = json.loads(response.text.replace(");", "").replace("getData(", ""), encoding="utf-8")
        # print(rs.get('data'))
        for i in rs.get('data').keys():
            # print(rs.get('data').get(i))
            item = SportteryItem()
            item['date'] = rs.get('data').get(i).get('b_date').replace('-','')
            item['cc'] = rs.get('data').get(i).get('num')[-3:]
            item['league'] = rs.get('data').get(i).get('l_cn')
            item['zhu'] = rs.get('data').get(i).get('h_cn')
            item['ke'] = rs.get('data').get(i).get('a_cn')
            item['half'] = ''
            item['full'] = ''
            item['w'] = rs.get('data').get(i).get('had').get('h') if rs.get('data').get(i).get('had') is not None else '0'
            item['p'] = rs.get('data').get(i).get('had').get('d') if rs.get('data').get(i).get('had') is not None else '0'
            item['l'] = rs.get('data').get(i).get('had').get('a') if rs.get('data').get(i).get('had') is not None else '0'
            item['sameIndex'] = rs.get('data').get(i).get('id')
            item['result'] = "https://i.sporttery.cn/api/fb_match_info/get_pool_rs/?f_callback=pool_prcess&mid=" + item[
                'sameIndex']
            item['same'] = "https://info.sporttery.cn/football/search_odds.php?mid=" + item['sameIndex']
            item['analysis'] = "https://i.sporttery.cn/api/fb_match_info/get_match_news_list?mid=" + item['sameIndex']
            # print(item)
            yield scrapy.Request(item['result'], meta={'item': item}, callback=self.parse_item)


    def parse_item(self, response):
        item = response.meta['item']
        rs = json.loads(response.text.replace(");", "").replace("pool_prcess(", ""), encoding="utf-8")
        # print(rs)
        if rs.get('status').get('code') == 0:
            item['had_odds'] = ''
            item['hhad_odds'] = ''
            item['crs_odds'] = ''
            item['ttg_odds'] = ''
            item['hafu_odds'] = ''
            item['had_prs_name'] = ''
            item['hhad_prs_name'] = ''
            item['crs_prs_name'] = ''
            item['ttg_prs_name'] = ''
            item['hafu_prs_name'] = ''
            h = rs.get('result').get('odds_list').get('had').get('odds')[-1].get('h')
            a = rs.get('result').get('odds_list').get('had').get('odds')[-1].get('a')
            d = rs.get('result').get('odds_list').get('had').get('odds')[-1].get('d')
            url = "https://i.sporttery.cn/api/fb_prize_odds/get_odds?f_call=get_odds&type=all&dan=0&h_odds={}&a_odds={}&d_odds={}".format(
                h, a, d)
            yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item1)

    def parse_item1(self, response):
        rs = json.loads(response.text.replace(")", "").replace("get_odds(", ""), encoding="utf-8")
        item = response.meta['item']
        total = int(len((rs.get('result')))) if rs.get('result') is not None else 0
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
        else:
            item['same_result'] = ' '
        yield scrapy.Request(item['analysis'], meta={'item': item}, callback=self.parse_item2)

    def parse_item2(self, response):
        item = response.meta['item']
        rs = json.loads(response.text, encoding="utf-8")
        print(rs)
        if rs.get('status').get('code') == 0:
            for i in rs.get('result'):
                if (i.get('adesc').split(' ')[0][-3:]) == item['cc'] or len(rs.get('result')) == 1:
                    yield scrapy.Request(i.get('url'), meta={'item': item}, callback=self.parse_item3)  # pass
        else:
            item['detail'] = ''
            url = 'https://i.sporttery.cn/api/cm_match_analys/get_match_data?f_callback=getData&mid=' + str(
                item['sameIndex'])
            yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item4)

    def parse_item3(self, response):
        item = response.meta['item']
        item['detail'] = "".join(
            response.xpath('//div[@class="con"]')[0].xpath('string(.)').extract()[0].strip().split())
        url = 'https://i.sporttery.cn/api/cm_match_analys/get_match_data?f_callback=getData&mid=' + str(
            item['sameIndex'])
        yield scrapy.Request(url, meta={'item': item}, callback=self.parse_item4)

    def parse_item4(self, response):
        item = response.meta['item']
        rs = json.loads(response.text.replace(");", "").replace("getData(", ""), encoding="utf-8")
        item['had_h_rate'] = rs.get('result').get('had_h_rate')
        item['had_d_rate'] = rs.get('result').get('had_d_rate')
        item['had_a_rate'] = rs.get('result').get('had_a_rate')
        # print(item)
        yield (item)



