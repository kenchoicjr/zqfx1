# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import datetime
import time
from zqfx.items import *


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZqfxPipeline(object):
    def __init__(self):
        dbargs = dict(host='127.0.0.1', db='zqfx', user='root',  # replace with you user name
                      passwd='admin',  # replace with you password
                      charset='utf8', cursorclass=MySQLdb.cursors.DictCursor, use_unicode=True, )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        self.start_time = datetime.datetime.now()

    def open_spider(self, spider):
        pass  # if spider.name == "fox008":  #     res = self.dbpool.runInteraction(self.del_table_fox008)  # elif spider.name == "live500":  #     res = self.dbpool.runInteraction(self.del_table_live500)

    def process_item(self, item, spider):
        if spider.name == "fox008":
            # mitem = ZqfxItem()
            if (isinstance(item, AnalysisItem)):  # ZqfxItem
                res = self.dbpool.runInteraction(self.del_table_analysis, item)
                time.sleep(0.7)
                res = self.dbpool.runInteraction(self.insert_into_table_analysis, item)
            elif (isinstance(item, ZqfxItem)):
                res = self.dbpool.runInteraction(self.del_table_fox008, item)
                time.sleep(0.7)
                res = self.dbpool.runInteraction(self.insert_into_table_fox008, item)
        elif spider.name == "live500":
            res = self.dbpool.runInteraction(self.del_table_live500, item)
            time.sleep(0.7)
            res = self.dbpool.runInteraction(self.insert_into_table_live500, item)
        elif spider.name == "vipc":
            # print("-"*1000)
            # print("-"*1000)
            res = self.dbpool.runInteraction(self.del_table_vipc, item)
            time.sleep(0.7)
            res = self.dbpool.runInteraction(self.insert_into_table_vipc, item)
        elif spider.name == "leisu":
            res = self.dbpool.runInteraction(self.del_table_leisu, item)
            time.sleep(0.7)
            res = self.dbpool.runInteraction(self.insert_into_table_leisu, item)
        else:
            pass
        return item

    def insert_into_table_fox008(self, conn, item):
        conn.execute('insert into zqfx(datec,cc,fxs_leauge,fxs_leauge_name0,fxs_leauge_name1,fxs_2_02_c01,'
                     'fxs_2_02_c03,fxs_2_03_gailus1,predictc,fxs_2_02_c01y,fxs_2_02_c01yp,fxs_2_02_c01yt,fxs_2_02_c01yg)'
                     'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                         item['date'], item['cc'], item['fxs_leauge'], item['fxs_leauge_name0'],
                         item['fxs_leauge_name1'], item['fxs_2_02_c01'], item['fxs_2_02_c03'], item['fxs_2_03_gailus1'],
                         item['predictc'], item['fxs_2_02_c01y'], item['fxs_2_02_c01yp'], item['fxs_2_02_c01yt'],
                         item['fxs_2_02_c01yg']))

    def insert_into_table_live500(self, conn, item):
        conn.execute('insert into live500(datec,cc,result,w,p,l,mar_right60,detail) values(%s,%s,%s,%s,%s,%s,%s,%s)', (
            item['date'], item['cc'], item['result'], item['w'], item['p'], item['l'], item['mar_right60'],
            item['detail']))

    def insert_into_table_leisu(self, conn, item):
        conn.execute(
            'insert into leisu(datec,team1,win,team2,lose,lsjf_left,lsjf_right,jqzj_left,jqzj_right,remarks,cc) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (item['date'], item['team1'], item['win'], item['team2'], item['lose'], item['lsjf_left'],
             item['lsjf_right'], item['jqzj_left'], item['jqzj_right'], item['remarks'], item['cc']))

    def insert_into_table_analysis(self, conn, item):
        conn.execute(
            "insert into tips(datec,cc,wjxs,slfx_left,slfx_right,sjfx_left,sjfx_rigft,wjjk_left,wjjk_rigft,op,yp,dzwj,_10cjk,pmxd) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (item['date'], item['cc'], item['wjxs'], item['slfx_left'], item['slfx_right'], item['sjfx_left'],
             item['sjfx_rigft'], item['wjjk_left'], item['wjjk_rigft'], item['op'], item['yp'], item['dzwj'],
             item['_10cjk'], item['pmxd']))

    def del_table_fox008(self, conn, item):
        sql = "DELETE  FROM zqfx where datec = '" + item['date'] + "' and cc = '" + item['cc'] + "'"
        conn.execute(sql)

    def del_table_live500(self, conn, item):
        sql = "DELETE  FROM live500 where datec = '" + item['date'] + "' and cc = '" + item['cc'] + "'"
        conn.execute(sql)

    def del_table_analysis(self, conn, item):
        sql = "DELETE  FROM tips where datec = '" + item['date'] + "' and cc = '" + item['cc'] + "'"
        conn.execute(sql)

    def del_table_leisu(self, conn, item):
        sql = "DELETE  FROM leisu where datec = '" + item['date'] + "' and team1 = '" + item['team1'] + "'"
        conn.execute(sql)

    def insert_into_table_vipc(self, conn, item):
        conn.execute('insert into vipc(datec,cc,win,lose,result,bf,url) values(%s,%s,%s,%s,%s,%s,%s)', (
            item['date'], item['cc'], item['win'], item['lose'], item['result'], item['bf'], item['url']))
    def del_table_vipc(self, conn, item):
        sql = "DELETE  FROM vipc where datec = '" + item['date'] + "' and cc = '" + item['cc'] + "'"
        conn.execute(sql)

def close_spider(self, spider):
    end_time = datetime.datetime.now()
    delta = end_time - self.start_time
    delta_gmtime = time.gmtime(delta.total_seconds())
    duration_str = time.strftime("%H:%M:%S", delta_gmtime)
    print("start time:", self.start_time)
    print("end time:", end_time)
    print("用时：", duration_str)
