# coding=utf-8
import requests
from lxml import etree
import json


class HsxyCasUtil(object):

    def get_list(self):
        # 1.根据url地址的规律,构造url list
        url = "http://appserver.midituan.com/jc/match"
        headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Mi Note 3 MIUI/V10.2.3.0.OCHCNFK)"
                   ,"Host": "appserver.midituan.com"}
        data = {"appPlatform": "3", "appType": "Android", "appVersion": "1.4.0", "licenseId": "227", "sid": "3452786",
                "token": "08ACA01149B6A3F0ED3B90385BB90668", "type": "hhgg", "umengchannel": "youMeng", "userId": 0}
        # 2.发送请求,获取响应
        response = requests.get(url, headers=headers, data=data)
        html_str = response.content.decode()
        # str = json.loads(html_str.replace('var llRWawxK=','').replace('pages:1,data','"data"'))
        # res = eval((html_str.replace('var NndphaDS=','')))
        print(
            html_str)  # print(html_str.replace('var NndphaDS={pages:1,data:','').replace('}',''))  # list=str['data']  # # print(list)  # gp_list = []  # print(len(list))  # for i in list:  #     print(i)  #     detail = i.split(',')  #     gp_list.append(detail)  # print(gp_list)  # return gp_list  # for i in list:  #     print(i)  # for i in res['jjcg']:  #     print(type(i))  # print(res['gdrs'])  # print(res['sdltgd'])  # print(res['sdgdcgbd'])  # print(res['sdgd'])  # html = etree.HTML(html_str)  # input_list = html.xpath("//form[@id='credentials']//input")  # # 3.提取数据  # # print(html.xpath("//input[@name='lt']/@value")[0])  # data = {}  # for input in input_list:  #     key = input.xpath("./@name")[0] if len(input.xpath("./@name")) > 0 else ""  #     value = input.xpath("./@value")[0]if len(input.xpath("./@value"))>0 else ""  #     if len(key) > 0 and len(value) > 0:  #         data[key] = value  # data["username"] = username  # data["password"] = password  # print(data)  # response = requests.post(url, headers=headers, cookies=cookie_dict, data=data)  # if response.content.decode().find(username)!= -1:  #     return username  # else:  #     return "-1"


if __name__ == '__main__':
    hsxyCasUtil = HsxyCasUtil()
    print(hsxyCasUtil.get_list())
