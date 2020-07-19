# coding=utf-8
import requests
from lxml import etree
import json
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from scrapy.http import HtmlResponse
import requests
from PIL import Image, ImageEnhance
import pytesseract
from selenium.webdriver.support.select import Select


class HsxyCasUtil(object):


    def get_list(self):
        image = Image.open("H:\\abc.jpg")
        # 图片转换成字符
        vcode = pytesseract.image_to_string(image)
        print("-------------------------------", vcode.strip())


if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())