# -*-coding: utf-8 -*-
__author__ = 'Yun'
import httplib2
from urllib import urlencode
import time
import random


def get_timestamp():
    return str(time.time()).replace('.', '') + str(random.randint(0, 9))


conn = httplib2.Http()
data = dict(login="327752822@qq.com", rememberMe=True, password="Bo89989136")
default_query_params = {
    "callback": "nike_Cart_hanleJCartResponse",
    "action": "addItem",
    "lang_locale": "zh_CN",
    "country": "CN",
    "catalogID": "1",
    "productID": "10188307",
    "price": "899.0",
    "siteId": None,
    "line1": "Nike Internationalist Mid QS",
    "line2": "男子运动鞋",
    "passcode": None,
    "sizeType": None,
    "skuAndSize": "11379170:40.5",
    "qty": "1",
    "rt": "json",
    "view": "3",
    "skuId": "11379170",
    "displaySize": "40.5",
    "_": get_timestamp()
}

login_resp, login_content = conn.request("https://www.nike.com/profile/login?Content-Locale=zh_CN", 'POST',
                                         urlencode(data),
                                         headers={'Content-Type': 'application/x-www-form-urlencoded'})
headers = {'Cookie': login_resp['set-cookie']}

product_resp, product_content = conn.request(
    "http://store.nike.com/cn/zh_cn/pd/internationalist-mid-qs-%E8%BF%90%E5%8A%A8%E9%9E%8B/pid-10188307/pgid-10053096",
    'GET', headers=headers)


headers['Cookie'] = product_resp['set-cookie']

temp_url = u"https://secure-store.nike.com/ap/services/jcartService?"
url = temp_url + urlencode(default_query_params)
print(url)
resp, content = conn.request(url, 'GET', headers=headers)

print resp, content



