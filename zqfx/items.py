# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZqfxItem(scrapy.Item):
    date = scrapy.Field()  # 比赛日期
    cc = scrapy.Field()  # 场次
    fxs_leauge = scrapy.Field()  # 联赛
    fxs_leauge_name0 = scrapy.Field()  # 主队
    fxs_leauge_name1 = scrapy.Field()  # 客队
    fxs_2_02_c01 = scrapy.Field()  # 彩种1
    fxs_2_02_c03 = scrapy.Field()  # 推荐1
    fxs_2_03_gailus1 = scrapy.Field()  # 概率1
    predictc = scrapy.Field()
    fxs_2_02_c01y = scrapy.Field()  # 彩种2
    fxs_2_02_c01yp = scrapy.Field()  # 盘口2
    fxs_2_02_c01yt = scrapy.Field()  # 推荐2
    fxs_2_02_c01yg = scrapy.Field()  # 概率2  # fxs_2_02_c01yp = scrapy.Field()  # pass


class ZqfxItem1(scrapy.Item):
    date = scrapy.Field()  # 比赛日期
    cc = scrapy.Field()  # 场次
    result = scrapy.Field()  # 结果
    w = scrapy.Field()  # 赔率
    p = scrapy.Field()
    l = scrapy.Field()
    mar_right60 = scrapy.Field()
    detail = scrapy.Field()


class AnalysisItem(scrapy.Item):
    date = scrapy.Field()  # 比赛日期
    cc = scrapy.Field()  # 场次
    wjxs = scrapy.Field()  # 往绩系数
    slfx_left = scrapy.Field()  # 实力分析左
    slfx_right = scrapy.Field()  # 实力分析右
    sjfx_left = scrapy.Field()  # 数据分析左
    sjfx_rigft = scrapy.Field()  # 数据分析右
    wjjk_left = scrapy.Field()  # 往绩近况左
    wjjk_rigft = scrapy.Field()  # 往绩近况右
    op = scrapy.Field()  # 欧赔
    yp = scrapy.Field()  # 亚赔
    dzwj = scrapy.Field()  # 对阵往绩
    _10cjk = scrapy.Field()  # 10场近况
    pmxd = scrapy.Field()  # 排名相当的近况


class LeisuItem(scrapy.Item):
    date = scrapy.Field()
    team1 = scrapy.Field()
    win = scrapy.Field()
    team2 = scrapy.Field()
    lose = scrapy.Field()
    lsjf_left = scrapy.Field()
    lsjf_right = scrapy.Field()
    jqzj_left = scrapy.Field()
    jqzj_right = scrapy.Field()
    remarks = scrapy.Field()
