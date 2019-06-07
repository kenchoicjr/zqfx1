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
        print(rs.get('data').keys())
