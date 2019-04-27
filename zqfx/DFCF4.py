# coding=utf-8
import requests
from lxml import etree
import json


class HsxyCasUtil(object):

    def get_list(self):
        # 1.根据url地址的规律,构造url list
        #//table[@id='hide_box_1']//tr[@mn='周六017']//input[@class='spArr']/@value
        url = "https://vipc.cn/jczq/singles"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"}

        # 2.发送请求,获取响应
        response = requests.get(url, headers=headers)
        html_str = response.content.decode()
        _element = etree.HTML(html_str)
        # str = json.loads(html_str.replace('var llRWawxK=','').replace('pages:1,data','"data"'))
        # res = eval((html_str.replace('var NndphaDS=','')))
        print(html_str)



if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
