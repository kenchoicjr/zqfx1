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
        url = "http://192.168.1.6/#hId-pgDevInfo"
        driver.get(url)
        time.sleep(10)
        printer_name = driver.find_element_by_xpath('//*[@id="appDevInfo-printerInfo-tbl-Tbl"]/tbody/tr[1]/td[2]').text
        printer_sno = driver.find_element_by_xpath('//*[@id="appDevInfo-printerInfo-tbl-Tbl"]/tbody/tr[3]/td[2]').text
        msg = {"printer_name": printer_name, "printer_sno": printer_sno}
        error_logs = ""
        for tr in trs:
            try:
                tr.find_element_by_xpath('.//div[@class="gui-icon-error w10"]')
            except Exception:
                pass
            else:
                error_log = tr.text + ";"
                error_logs += error_log

        msg["error_logs"] = error_logs
        driver.quit()
        time.sleep(2)
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                   options=options)
        url = "http://192.168.1.6/#hId-pgConsumables"
        driver.get(url)
        time.sleep(10)
        yellow_ink_status = driver.find_element_by_xpath(
            '//*[@id="appConsumable-inkCart-tbl-Tbl"]/tbody/tr[9]/td[2]').text
        magenta_ink_status = driver.find_element_by_xpath(
            '//*[@id="appConsumable-inkCart-tbl-Tbl"]/tbody/tr[9]/td[3]').text
        blue_ink_status = driver.find_element_by_xpath(
            '//*[@id="appConsumable-inkCart-tbl-Tbl"]/tbody/tr[9]/td[4]').text
        black_ink_status = driver.find_element_by_xpath(
            '//*[@id="appConsumable-inkCart-tbl-Tbl"]/tbody/tr[9]/td[5]').text
        msg["yellow_ink_status"] = yellow_ink_status
        msg["magenta_ink_status"] = magenta_ink_status
        msg["blue_ink_status"] = blue_ink_status
        msg["black_ink_status"] = black_ink_status

        driver.quit()

        time.sleep(2)
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',
                                   options=options)
        url = "https://192.168.1.6/#hId-pgTrayAndPaperMgmt"
        driver.get(url)
        time.sleep(10)
        tray2_status = driver.find_element_by_xpath('//*[@id="tray_and_paper_settings-Tbl"]/tbody/tr[2]/td[2]/div').text
        # print(tray_status)
        msg["tray2_status"] = tray2_status
        driver.quit()

        return msg


if __name__ == '__main__':
    PrinterUtil = PrinterUtil()
    print(PrinterUtil.get_status())
