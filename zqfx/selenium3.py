# coding=utf-8
import requests
from lxml import etree
import json
import datetime
from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class HsxyCasUtil(object):

    def get_list(self):
        # return ['2638379']
        # driver = webdriver.PhantomJS(executable_path=r'M:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        d = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        # print(d)
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe', options=options)
        url = "http://jc.win007.com/index.aspx"
        # http: // jc.win007.com / index.aspx
        # http: // jc.win007.com / schedule.aspx?d = 2019 - 10 - 19
        driver.get(url)
        # time.sleep(6)
        html = driver.execute_script('return document.documentElement.outerHTML')
        lists = []
        dict = {"周日": "0", "周一": "1", "周二": "2", "周三": "3", "周四": "4", "周五": "5", "周六": "6"}
        elems = driver.find_elements_by_tag_name("tr")
        # html = driver.execute_script('return document.documentElement.outerHTML')
        # print(elems.gettext)
        for elem in elems:
            if elem.get_attribute("name") is not None and elem.get_attribute("id") is not None and elem.get_attribute(
                    "style") != "display: none;":
                # lists.append(elem.get_attribute("data-id"))

                if elem.get_attribute("id")[:3] == "tr1":
                    # print(elem.get_attribute("id")[-7:])
                    # print(elem.find_elements_by_tag_name("div")[0].text)
                    # print(elem.find_elements_by_tag_name("div")[0].text[:2])
                    y = dict[elem.find_elements_by_tag_name("div")[0].text[:2]]
                    # print(y)
                    d=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=int(y)), '%Y-%m-%d')
                    lists.append(elem.get_attribute("id")[-7:]+"*"+d+"*"+elem.find_elements_by_tag_name("div")[0].text)
                else:
                    pass
            else:
                pass
        # print(len(lists))
        # print(driver.page_source)
        driver.quit()
        return lists


if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
