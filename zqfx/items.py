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
    cc = scrapy.Field()


class VipcItem(scrapy.Item):
    date = scrapy.Field()
    cc = scrapy.Field()
    win = scrapy.Field()
    lose = scrapy.Field()
    result = scrapy.Field()
    bf = scrapy.Field()
    url = scrapy.Field()


class SportteryItem(scrapy.Item):
    date = scrapy.Field()
    cc = scrapy.Field()
    league = scrapy.Field()
    zhu = scrapy.Field()
    ke = scrapy.Field()
    half = scrapy.Field()
    full = scrapy.Field()
    w = scrapy.Field()
    p = scrapy.Field()
    l = scrapy.Field()
    result = scrapy.Field()
    analysis = scrapy.Field()
    same = scrapy.Field()
    had_odds = scrapy.Field()
    hhad_odds = scrapy.Field()
    crs_odds = scrapy.Field()
    ttg_odds = scrapy.Field()
    hafu_odds = scrapy.Field()
    had_prs_name = scrapy.Field()
    hhad_prs_name = scrapy.Field()
    crs_prs_name = scrapy.Field()
    ttg_prs_name = scrapy.Field()
    hafu_prs_name = scrapy.Field()
    same_result = scrapy.Field()
    sameIndex = scrapy.Field()
    had_h_rate = scrapy.Field()
    had_d_rate = scrapy.Field()
    had_a_rate = scrapy.Field()
    detail = scrapy.Field()


class Win007Item(scrapy.Item):
    date = scrapy.Field()  # 比赛日期
    cc = scrapy.Field()  # 场次
    mar_right60 = scrapy.Field()
    detail = scrapy.Field()
    url = scrapy.Field()
    mar_right1 = scrapy.Field()
    mar_right2 = scrapy.Field()
    mar_right3 = scrapy.Field()
    mar_right4 = scrapy.Field()
    mar_right5 = scrapy.Field()
    mar_right6 = scrapy.Field()
    match_time = scrapy.Field()
    home_team = scrapy.Field()
    guest_team = scrapy.Field()
    h_odd = scrapy.Field()
    pk = scrapy.Field()
    g_odd = scrapy.Field()
    full_result = scrapy.Field()
    asian_odds_url = scrapy.Field()
    oddslist_url = scrapy.Field()
    oddstr_281 = scrapy.Field()
    oddstr_115 = scrapy.Field()
    oddstr_82 = scrapy.Field()
    odds_3 = scrapy.Field()
    odds_8 = scrapy.Field()
    odds_14 = scrapy.Field()
    oddstr_281_f_result = scrapy.Field()
    oddstr_281_l_result = scrapy.Field()
    oddstr_115_f_result = scrapy.Field()
    oddstr_115_l_result = scrapy.Field()
    oddstr_82_f_result = scrapy.Field()
    oddstr_82_l_result = scrapy.Field()
    odds_3_f_result = scrapy.Field()
    odds_3_l_result = scrapy.Field()
    odds_8_f_result = scrapy.Field()
    odds_8_l_result = scrapy.Field()
    odds_14_f_result = scrapy.Field()
    odds_14_l_result = scrapy.Field()
