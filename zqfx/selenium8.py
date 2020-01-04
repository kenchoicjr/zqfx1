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
        options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')

        driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',options=options)
        url = "http://order.neea.cn/readingAgreement/toAgreement?proId=13&amp;articleId=1475&amp;cbd=knight"
        driver.get(url)
        driver.implicitly_wait(10)
        elem = driver.find_element_by_id("loginName")
        elem.send_keys("kenchoicjr@126.com")
        elem = driver.find_element_by_id("loginPwd")
        elem.send_keys("Cjr19801021")
        # time.sleep(5)
        driver.find_element_by_id("verificationCode").clear()
        location = driver.find_element_by_id('kaptchaImage').location
        size = driver.find_element_by_id('kaptchaImage').size
        screenImg = "H:\screenImg.png"
        driver.get_screenshot_as_file(screenImg)
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        a = Image.open("H:\screenImg.png")
        im = a.crop((left, top, right, bottom))
        im = im.convert('RGBA')  # 转换模式：L | RGB
        im = im.convert('L')  # 转换模式：L | RGB
        im = ImageEnhance.Contrast(im)  # 增强对比度
        im = im.enhance(1.0)  # 增加饱和度
        im.save('H:\screenImg.png')
        time.sleep(1)
        # 打开保存的验证码图片
        image = Image.open("H:\screenImg.png")
        # 图片转换成字符
        vcode = pytesseract.image_to_string(image)
        print(vcode.strip())

        # img = img.convert('RGBA')  # 转换模式：L | RGB
        # img = img.convert('L')  # 转换模式：L | RGB
        # img = ImageEnhance.Contrast(img)  # 增强对比度
        # img = img.enhance(2.0)  # 增加饱和度
        # img.save(screenImg)
        # img = Image.open(screenImg)
        # code = pytesseract.image_to_string(img)
        # print(code.strip())
        time.sleep(5)
        elem = driver.find_element_by_id("login_button")
        elem.click()
        driver.implicitly_wait(10)
        elems = driver.find_elements_by_tag_name("input")
        for elem in elems:
            if elem.get_attribute('value')=="同意":
                # elem.click()
                driver.execute_script("arguments[0].click();", elem)
                break
        driver.implicitly_wait(10)
        time.sleep(1)
        ac = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div/div/div[1]/div[1]/dl[2]/dd/select')
        # //*[@id="layout-screen"]/div[1]/div/div[2]/a[1]
        ActionChains(driver).double_click(ac).perform()
        # print(driver.page_source)
        time.sleep(1)
        elems = driver.find_elements_by_tag_name("a")
        for elem in elems:
            if elem.get_attribute('attrval')=='202013002':
                elem.click()
                break
        # elem = driver.find_elements_by_tag_name("addr")[0]
        # elem.click()

        # driver.execute_script("arguments[0].onchange();", elem)
        driver.implicitly_wait(10)
        time.sleep(1)
        Select(driver.find_element_by_name("addr")).select_by_visible_text("广东省")
        driver.implicitly_wait(10)
        time.sleep(1)
        elems = driver.find_elements_by_tag_name("a")
        for elem in elems:
            if elem.text == '暨南大学（广州番禺执信中学考点）':
                elem.click()
                break
        driver.implicitly_wait(10)
        time.sleep(1)
        while True:
            time.sleep(1)
            elems = driver.find_elements_by_tag_name("a")
            for elem in elems:
                if elem.text == 'KET青少版':
                    elem.click()
                    break
            time.sleep(1)
            driver.implicitly_wait(10)
            # elem = driver.find_element_by_id("submit_but")
            elem = driver.find_element_by_id("submit_but")
            if elem.is_displayed():
                break


            # elems = driver.find_elements_by_tag_name("a")
            # for elem in elems:
            #     if elem.text == 'KET青少版':
            #         elem.click()
            #         break
            # time.sleep(1)
            # elems = driver.find_elements_by_tag_name("a")
            # for elem in elems:
            #     if elem.text == 'PET青少版':
            #         elem.click()
            #         break
        driver.implicitly_wait(10)
        time.sleep(1)
        elem = driver.find_element_by_id("submit_but")
        # elem.click()
        # print("-------------------------------------------"+elem.text)
        # print(driver

        # print(driver.page_source)
        # response_selenium = driver.page_source  # 响应内容
        # print(response_selenium)
        # time.sleep(1.8)
        # driver.quit()
        # return HtmlResponse(url=driver.current_url, body=response_selenium, encoding='utf-8')



if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
