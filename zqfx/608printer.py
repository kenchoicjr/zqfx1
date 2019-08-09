# coding=utf-8
import requests
from lxml import etree
import json
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import datetime


class PrinterUtil(object):

    def get_status(self):
        msg = {}
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                   options=options)
        url = "https://192.168.1.3/hp/device/InternalPages/Index?id=ConfigurationPage"
        driver.get(url)
        time.sleep(10)
        printer_name = driver.find_element_by_xpath('//*[@id="ProductName"]').text
        printer_sno = driver.find_element_by_xpath('//*[@id="SerialNumber"]').text
        msg = {"printer_name": printer_name, "printer_sno": printer_sno}
        driver.quit()
        time.sleep(2)
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                   options=options)
        url = "https://192.168.1.3/hp/device/InternalPages/Index?id=SuppliesStatus"
        driver.get(url)
        time.sleep(10)
        black_PagesRemaining = driver.find_element_by_xpath(
            '//*[@id="BlackCartridge1-EstimatedPagesRemaining"]').text
        msg["black_PagesRemaining"] = black_PagesRemaining
        blackCartridge1 = driver.find_element_by_xpath(
            '//*[@id="BlackCartridge1-Header_Level"]').text
        msg["blackCartridge1"] = blackCartridge1
        driver.quit()
        time.sleep(2)
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                   options=options)
        url = "https://192.168.1.3/hp/device/DeviceStatus/Index"
        driver.get(url)
        time.sleep(10)
        tray2_status = driver.find_element_by_xpath('//*[@id="TrayBinStatus_2"]').text
        msg["tray2_status"] = tray2_status
        error_logs = ""
        error_logs = driver.find_element_by_xpath('//*[@id="MachineStatus"]').text
        msg["error_logs"] = error_logs
        driver.quit()
        return msg


if __name__ == '__main__':
    PrinterUtil = PrinterUtil()
    print(PrinterUtil.get_status())
