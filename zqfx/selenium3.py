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
        dict = {"周日": "6", "周一": "0", "周二": "1", "周三": "2", "周四": "3", "周五": "4", "周六": "5"}
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

                    y = int(dict[elem.find_elements_by_tag_name("div")[0].text[:2]]) - int(
                        datetime.datetime.now().weekday())
                    # print(y)
                    if url.find("d=") > 0:
                        match_date = url[url.find("d=")+2:]
                        # print(match_date)
                    else:
                        match_date = datetime.datetime.strftime(
                            datetime.datetime.now() + datetime.timedelta(days=int(y)),
                            '%Y-%m-%d')
                    d = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=int(y)),
                                                   '%Y-%m-%d')
                    match_time = elem.find_elements_by_tag_name("td")[2].text
                    match_id = elem.get_attribute("id")[-7:]
                    match_weekday = elem.find_elements_by_tag_name("div")[0].text
                    home_team = elem.find_elements_by_tag_name("td")[4].text
                    full_result_str = elem.find_elements_by_tag_name("td")[5].find_elements_by_tag_name("div")[0].text
                    # print(len(full_result_str))
                    full_result_list = full_result_str.split("-")
                    home_s, guest_s = full_result_list
                    # print(home_s, guest_s)
                    if len(full_result_str) < 3:
                        full_result = ""
                    elif int(home_s) > int(guest_s):
                        full_result = "主胜"
                    elif int(home_s) < int(guest_s):
                        full_result = "客胜"
                    elif int(home_s) == int(guest_s):
                        full_result = "平手"
                    else:
                        full_result = ""
                    guest_team = elem.find_elements_by_tag_name("td")[6].text
                    h_odd = elem.find_elements_by_tag_name("td")[8].text
                    pk = elem.find_elements_by_tag_name("td")[9].text
                    g_odd = elem.find_elements_by_tag_name("td")[10].text
                    print(match_id, match_date, match_weekday, match_time, home_team, guest_team, h_odd, pk, g_odd)
                    lists.append(match_id + "*" + match_date + "*" + match_weekday + "*" + match_time + "*" + home_team
                                 + "*" + guest_team + "*" + h_odd + "*" + pk + "*" + g_odd + "*" + full_result)
                else:
                    pass
            else:
                pass
        # print(lists)
        # print(driver.page_source)
        driver.quit()
        # print(datetime.datetime.now().weekday())
        # return ['1734229*2019-11-09*周六018*22:30*沙尔克04*杜塞多夫*1.52*3.85*4.90*平手']
        return lists


if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
