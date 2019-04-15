# coding=utf-8
import requests
from lxml import etree
import json


class HsxyCasUtil(object):

    def get_list(self):
        # 1.根据url地址的规律,构造url list
        #url = "http://www.fox008.com/analysis/tips/20190330201.html"
        url ="http://www.fox008.com/analysis/tips/20190405001.html"
        #//table[@id='table_match']//td[@class='red'][2]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36"}

        # 2.发送请求,获取响应
        response = requests.get(url, headers=headers)
        html_str = response.content.decode()
        # print(html_str)
        _element = etree.HTML(html_str)
        left = _element.xpath("//div[@id='capacityV1']//td[@align='left']/text()")[0]
        right = _element.xpath("//div[@id='capacityV1']//td[@align='right']/text()")[0]
        print(left,right)
        # left_1 = _element.xpath("//div[@class='fx_qb_left350'][1]/div[contains(@class,'fx_qb_list')]/p/text()")
        # left_2 = _element.xpath("//div[@class='fx_qb_left350'][2]/div[contains(@class,'fx_qb_list')]/p/text()")
        # left_3 = _element.xpath("//div[@class='fx_qb_left350'][3]/div[contains(@class,'fx_qb_list')]/p/text()")
        # print('\n'.join(left_1))
        # print('\n'.join(left_2))
        # print('\n'.join(left_3))
        # right_1 = _element.xpath("//div[@class='fx_qb_rig350'][1]/div[contains(@class,'fx_qb_list')]/p/text()")
        # right_2 = _element.xpath("//div[@class='fx_qb_rig350'][2]/div[contains(@class,'fx_qb_list')]/p/text()")
        # right_3 = _element.xpath("//div[@class='fx_qb_rig350'][3]/div[contains(@class,'fx_qb_list')]/p/text()")
        # print('\n'.join(right_1))
        # print('\n'.join(right_2))
        # print('\n'.join(right_3))
        data1 = _element.xpath("//div[@class='fx_qb_m300']/table[1]//tr/td[@align='left']/span/text()")
        print(''.join(data1))
        data2 = _element.xpath("//div[@class='fx_qb_m300']/table[1]//tr/td[@align='center']/span/text()")
        print(''.join(data2))
        data3 = _element.xpath("//div[@class='fx_qb_m300']/table[1]//tr/td[@align='right']/span/text()")
        print(''.join(data3))
        data4 = _element.xpath("//div[@class='fx_qb_m300']/table[3]//tr/td[@align='left']/span/text()")
        print(''.join(data4))
        data5 = _element.xpath("//div[@class='fx_qb_m300']/table[3]//tr/td[@align='center']/span/text()")
        print(''.join(data5))
        data6 = _element.xpath("//div[@class='fx_qb_m300']/table[3]//tr/td[@align='right']/span/text()")
        print(''.join(data6))
        data7 = _element.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/div/span/text()")
        data8 = _element.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/span/text()")
        data8_1 = _element.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='left']/span/span/text()")
        data9 = _element.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/div/span/text()")
        data10 = _element.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/span/text()")
        data10_1 = _element.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='right']/span/span/text()")
        data11 = _element.xpath("//div[@class='fx_qb_nor'][1]/table[1]//tr/td[@align='center'][1]/text()")
        print(''.join(data7[:6]),''.join(data8[:2]),data11[0],''.join(data9[:6]), ''.join(data10[:2]))
        print(''.join(data10[3:5]))
        print(''.join(data7[12:18]),''.join(data8[5:7]),data11[2],''.join(data9[12:18]), ''.join(data10[5:7]))  # print(data11[0])  # print(data11[1])  # print(data11[2])  # print(''.join(data9[:6]), ''.join(data10[:2]))  # print(''.join(data9[6:12]), ''.join(data10[2:3]) + data10_1[0] + ''.join(data10[3:5]))  # print(''.join(data9[12:18]), ''.join(data10[5:7]))
        # // script[ @ type = 'text/javascript'][5]
        # str = json.loads(html_str.replace('var liveOddsList=','data'))
        # res = eval((html_str.replace('var NndphaDS=','')))
        # print(Re_json)
        # print(html_str.replace('var NndphaDS={pages:1,data:','').replace('}',''))
        # list=str(Re_json)
        # # print(list)
        # str1 = list.replace('var liveOddsList=', '')
        # # print(eval(str1))
        # list2=eval(str1)
        # # data = json.loads(list2[0])
        # json1 = (json.loads(list2[0].replace(";", "")))
        # print(json1)

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
