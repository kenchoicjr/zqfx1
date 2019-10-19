# coding=utf-8
import requests
from lxml import etree
import json
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class HsxyCasUtil(object):

    def get_list(self):
        # return ['2638379']
        # driver = webdriver.PhantomJS(executable_path=r'M:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',options=options)
        url = "http://jc.win007.com/index.aspx"
        driver.get(url)
        # time.sleep(6)
        html = driver.execute_script('return document.documentElement.outerHTML')
        print(driver.page_source)
        driver.quit()



if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
