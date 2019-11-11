import base64
import requests
import time
import random
import json

def base_code(username, password):
    str = '%s:%s' % (username, password)
    encodestr = base64.b64encode(str.encode('utf-8'))
    return '%s' % encodestr.decode()

def main():
    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'cookie':'__guid=172500851.2340334803851341000.1573347463752.8755; monitor_count=1',#cookie要自己更新一下！！！！！！
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    }
    username = 'kenchoicjr@126.com' #这里填入用户名！！！！！
    password = 'Cjr19801021'# 这里填入密码！！！！！
    base = base_code(username, password)
    print(base)
    DEFAULT_REQUEST_HEADERS['Proxy-Authorization'] = 'Basic '+base
    url = r'https://h.wandouip.com/get/ip-list?pack=%s&num=1&xy=1&type=2&lb=\r\n&mr=1&' % random.randint(100,1000)
    response = requests.get(url=url,headers=DEFAULT_REQUEST_HEADERS)
    print(response.text)
    text = json.loads(response.text)
    ip = text['data'][0]['ip']
    port = text['data'][0]['port']
    proxy = {'http': '%s:%s' % (ip, port)}

    # url_1 = 'http://www.baiduyunpan.org/thread-31333-1-1.html?x=328738'
    url_1 = 'http://httpbin.org/ip'

    r1 = requests.get(url_1, headers=DEFAULT_REQUEST_HEADERS, proxies=proxy)
    # time.sleep(random.randint(1, 3))
    print(response.text)
    # print(r1.text)

if __name__ == '__main__':
    for i in range(20):
        main()
        print('成功获取IP数量: '+str(i+1))
