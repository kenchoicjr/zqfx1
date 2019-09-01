# coding=utf-8
import requests
from lxml import etree
import json
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import datetime


class CasUtil(object):

    @staticmethod
    def cas(username, password):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                   options=options)
        url = "https://cas.scau.edu.cn/lyuapServer/login"
        driver.get(url)
        driver.implicitly_wait(20)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        ac = driver.find_element_by_xpath('//*[@class="btn-submit"]')
        ActionChains(driver).double_click(ac).perform()
        driver.implicitly_wait(5)
        xh = "-1"
        try:
            msg = driver.find_element_by_xpath('//*[@id="msg"]').text
        except:
            div = driver.find_element_by_xpath('//*[@id="_studentinfo_WAR_cas4foruserportlet_userinfo"]')
            driver.implicitly_wait(20)
            tds = div.find_elements_by_tag_name("td")
            for td in tds:
                if td.text.find(username) > 0:
                    xh = username
                    break
            ac = driver.find_element_by_xpath('//*[@class="exit"]')
            ActionChains(driver).double_click(ac).perform()
            driver.quit()
            return xh
        if msg == "账号或密码错误":
            driver.quit()
            return xh


if __name__ == '__main__':
    hnnydxCasUtil = CasUtil()
    print(hnnydxCasUtil.cas("201514040116", "741852963ouou"))
