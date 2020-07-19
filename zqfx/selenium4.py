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
        urls = ['https://live.500.com/index.php?e=' + datetime.datetime.strftime(
            datetime.datetime.now() + datetime.timedelta(days=-1),
            '%Y-%m-%d'),
                'https://live.500.com/index.php?e=' + datetime.datetime.strftime(
                    datetime.datetime.now() + datetime.timedelta(days=-2),
                    '%Y-%m-%d'),
                'https://live.500.com/index.php?e=' + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')]
        # http: // jc.win007.com / index.aspx
        # http: // jc.win007.com / schedule.aspx?d = 2019 - 10 - 19
        lists = []
        for url in urls:
            driver.get(url)
            elems = driver.find_elements_by_tag_name("tr")
            # html = driver.execute_script('return document.documentElement.outerHTML')
            # print(elems.gettext)
            for elem in elems:
                if elem.get_attribute("fid") is not None:
                    # lists.append(elem.get_attribute("data-id"))

                    if len(elem.get_attribute("fid")) == 6 and elem.find_elements_by_tag_name("td")[10].get_attribute(
                            "class") == "red":
                        # http://odds.500.com/fenxi/shuju-869820.shtml
                        # print(elem.get_attribute("fid"))
                        # if elem.find_elements_by_tag_name("td")[10].get_attribute("class") == "red":
                        # print(elem.find_elements_by_tag_name("td")[10].text)
                        # print(len(elem.find_elements_by_tag_name("td")[9].text))
                        if len(elem.find_elements_by_tag_name("td")[9].text) == 12:
                            # print(elem.find_elements_by_tag_name("td")[9].text[:4])
                            # print(elem.find_elements_by_tag_name("td")[9].text[4:8])
                            # print(elem.find_elements_by_tag_name("td")[9].text[8:])
                            lists.append(
                                url[-10:] + "*" + elem.find_elements_by_tag_name("td")[0].text + "*" +
                                elem.find_elements_by_tag_name("td")[9].text[:4] + "*" +
                                elem.find_elements_by_tag_name("td")[9].text[4:8] + "*" +
                                elem.find_elements_by_tag_name("td")[9].text[8:] + "*" +
                                elem.find_elements_by_tag_name("td")[10].text + "*" +
                                "http://odds.500.com/fenxi/shuju-{}.shtml".format(elem.get_attribute("fid"))+ "*" +
                                elem.get_attribute("fid")
                            )
                        else:
                            lists.append(
                                url[-10:] + "*" + elem.find_elements_by_tag_name("td")[0].text + "*" +
                                "0" + "*" +
                                "0" + "*" +
                                "0" + "*" +
                                elem.find_elements_by_tag_name("td")[10].text + "*" +
                                "http://odds.500.com/fenxi/shuju-{}.shtml".format(elem.get_attribute("fid"))+ "*" +
                                elem.get_attribute("fid")
                            )

                    else:
                        pass
                else:
                    pass
            print(len(lists))
        # time.sleep(6)
        html = driver.execute_script('return document.documentElement.outerHTML')

        dict = {"周日": "6", "周一": "0", "周二": "1", "周三": "2", "周四": "3", "周五": "4", "周六": "5"}

        # print(driver.page_source)
        driver.quit()
        # print(datetime.datetime.now().weekday())
        return lists


if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
