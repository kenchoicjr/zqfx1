# coding=utf-8
import requests
from lxml import etree
import json
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import datetime
from scrapy.http import HtmlResponse

class HsxyCasUtil(object):

    def get_list(self):
        dates=[]
        dates.append(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d'))
        dates.append(datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=+1),
                                                               '%Y%m%d'))
        lists = []

        for d in dates:
            options = webdriver.FirefoxOptions()
            options.add_argument('-headless')
            driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                       options=options)
            url = "https://live.leisu.com/saicheng?date="+d
            driver.get(url)
            cookie = {}
            for i in driver.get_cookies():
                cookie[i["name"]] = i["value"]
            with open("cookies.txt", "w") as f:
                f.write(json.dumps(cookie))
            # ac = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/a[1]')
            # # //*[@id="layout-screen"]/div[1]/div/div[2]/a[1]
            # ActionChains(driver).double_click(ac).perform()
            time.sleep(2)
            elems = driver.find_elements_by_tag_name("li")
            for elem in elems:
                if elem.get_attribute("data-id") is not None and "周" in elem.get_attribute("data-lottery"):
                    # print(elem.get_attribute("data-lottery"))

                    lists.append(elem.get_attribute("data-id")+"-"+elem.get_attribute("data-lottery").split(",")[0])
                else:
                    pass
            lists = list(set(lists))
            # print(len(lists))

            driver.quit()
        return lists

    def re(self,url):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',options=options)
        url = url
        driver.get(url)
        # time.sleep(1.8)
        # html = driver.execute_script('return document.documentElement.outerHTML')
        # print(html)
        #
        driver.implicitly_wait(10)
        response_selenium = driver.page_source  # 响应内容
        # print(response_selenium)
        time.sleep(1.8)
        driver.quit()
        return HtmlResponse(url=driver.current_url, body=response_selenium, encoding='utf-8')


if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
