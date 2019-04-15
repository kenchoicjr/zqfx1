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
        url = "https://live.leisu.com/"
        driver.get(url)

        ac = driver.find_element_by_xpath('//*[@id="layout-screen"]/div/div/div[2]/a[1]')
        ActionChains(driver).double_click(ac).perform()
        ac = driver.find_element_by_xpath('//*[@id="music"]')
        ActionChains(driver).move_to_element(ac).perform()
        ac = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[4]/div/ul/li[1]')
        ActionChains(driver).click(ac).perform()
        # ac = driver.find_element_by_xpath('//*[@id="layout-screen"]/div/div/div[2]/a[1]').click()
        time.sleep(2)
        # driver.save_screenshot("1.png")
        # driver.refresh()
        # print(driver)
        # driver.save_screenshot("1.png")
        # driver.refresh()
        # time.sleep(5)
        # driver.save_screenshot("2.png")
        # html = driver.execute_script('return document.documentElement.outerHTML')
        # print(html)
        lists =[]
        elems = driver.find_elements_by_tag_name("tr")
        # html = driver.execute_script('return document.documentElement.outerHTML')

        for elem in elems:
            if elem.get_attribute("data-id") is not None and elem.get_attribute("style") != "display: none;":
                lists.append(elem.get_attribute("data-id"))
            else:
                pass
        print(len(lists))
        # driver.quit()
        return lists


# if __name__ == '__main__':
#     hsxyCasUtil = HsxyCasUtil()
#     print(hsxyCasUtil.get_list())
