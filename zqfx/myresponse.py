# coding=utf-8
import requests
from lxml import etree
import json
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from scrapy.http import HtmlResponse
import requests


class MyResponse(object):

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        print("init")
        self.driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe', options=options)

    def get_list(self, url):
        # url = "https://vipc.cn/jczq/singles/2019-12-23"
        self.driver.get(url)
        # time.sleep(1.8)
        # html = driver.execute_script('return document.documentElement.outerHTML')
        # print(html)
        response_selenium = self.driver.page_source  # 响应内容
        print("get_list")
        # time.sleep(1.8)
        # driver.quit()
        return HtmlResponse(url=self.driver.current_url, body=response_selenium, encoding='utf-8')

    def close_driver(self):
        print("close_driver")
        self.driver.quit()


if __name__ == '__main__':
    url = "https://vipc.cn/jczq/singles/2019-12-23"
    myResponse = MyResponse()
    print(myResponse.get_list(url))
    myResponse.close_driver()
