# coding=utf-8
import requests
from lxml import etree
import json


class HsxyCasUtil(object):

    def get_list(self):
        # 1.根据url地址的规律,构造url list
        #//table[@id='hide_box_1']//tr[@mn='周六017']//input[@class='spArr']/@value
        url = "https://live.leisu.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"}

        # 2.发送请求,获取响应
        response = requests.get(url, headers=headers)
        html_str = response.content.decode()
        _element = etree.HTML(html_str)
        # str = json.loads(html_str.replace('var llRWawxK=','').replace('pages:1,data','"data"'))
        # res = eval((html_str.replace('var NndphaDS=','')))
        # print(html_str)
        Re_json = _element.xpath("//script[@id='LoadOkRemove']/text()")
        list = str(Re_json)
        # print(list)
        str1 = list.find('THATDATA={"')
        str2=list[str1:].find("]}};")
        print(str2)
        # list=str['data']
        json1=(list[str1:][:str2+4])
        print(json.loads(json1.replace("THATDATA=","").replace(";","").replace('\\"','"')))
        # gp_list = []
        # print(len(list))
        # for i in list:
        #     print(i)
        #     detail = i.split(',')
        #     gp_list.append(detail)
        # print(gp_list)
        # return gp_list
        # for i in list:
        #     print(i)
        # for i in res['jjcg']:
        #     print(type(i))
        # print(res['gdrs'])
        # print(res['sdltgd'])
        # print(res['sdgdcgbd'])
        # print(res['sdgd'])
        # html = etree.HTML(html_str)
        # input_list = html.xpath("//form[@id='credentials']//input")
        # # 3.提取数据
        # # print(html.xpath("//input[@name='lt']/@value")[0])
        # data = {}
        # for input in input_list:
        #     key = input.xpath("./@name")[0] if len(input.xpath("./@name")) > 0 else ""
        #     value = input.xpath("./@value")[0]if len(input.xpath("./@value"))>0 else ""
        #     if len(key) > 0 and len(value) > 0:
        #         data[key] = value
        # data["username"] = username
        # data["password"] = password
        # print(data)
        # response = requests.post(url, headers=headers, cookies=cookie_dict, data=data)
        # if response.content.decode().find(username)!= -1:
        #     return username
        # else:
        #     return "-1"


if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
