# coding=utf-8
import requests
from lxml import etree
import json
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from scrapy.http import HtmlResponse
import requests


class HsxyCasUtil(object):

    def get_list(self):
        options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')

        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',options=options)
        url = "https://vipc.cn/jczq/singles/2019-12-23"
        driver.get(url)
        # time.sleep(1.8)
        # html = driver.execute_script('return document.documentElement.outerHTML')
        # print(html)

        response_selenium = driver.page_source  # 响应内容
        # print(response_selenium)
        # time.sleep(1.8)
        # driver.quit()
        return HtmlResponse(url=driver.current_url, body=response_selenium, encoding='utf-8')



if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
