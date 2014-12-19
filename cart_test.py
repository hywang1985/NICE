# coding: utf-8
__author__ = 'Yun'

import httplib2
from urllib import urlencode
import random
import time


def get_timestamp():
    return str(time.time()).replace('.', '') + str(random.randint(0, 9))


def analysis_cookie(cookie_string):
    cookie_list = cookie_string.split(";")
    cookie_dict = dict()
    for c in cookie_list:
        c = c.strip()
        cookie_dict[c.split('=')[0]] = c.split('=')[1]
    return cookie_dict


def get_cart_page():
    conn = httplib2.Http()
    url = "https://secure-store.nike.com/cn/checkout/html/cart.jsp?country=CN&country=CN&l=cart"
    resp, content = conn.request(url, 'GET')
    print resp['set-cookie']
    return resp


def get_cart(header):
    conn = httplib2.Http()
    url = "https://secure-store.nike.com/ap/services/jcartService?"
    params = {
        "callback": "jQuery17209916341905482113_1418974596574",
        "action": "getCartSummary",
        "rt": "json",
        "country": "CN",
        "lang_locale": "zh_CN",
        "_": get_timestamp()
    }
    resp, content = conn.request(url, 'GET', urlencode(params), headers={'Cookie': header})
    print resp
    return resp


def add_goods_to_cart(header):
    conn = httplib2.Http()
    url = "https://secure-store.nike.com/ap/services/jcartService?"
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
    url = url + urlencode(default_query_params)
    resp = conn.request(url, 'GET', headers={'Cookie': header})
    print resp
    return resp


if __name__ == '__main__':
    # headers = get_cart_page().get('set-cookie', None)
    # add_goods_to_cart(headers)
    cookie = 'slsw=N:Q; RES_TRACKINGID=663135396782308; s_vi=[CS]v1|2A49F7CE0501182C-600016068002878C[CE]; AnalysisUserId=210.192.118.4.237011418981295503; NIKE_COMMERCE_CCR=1418981220412; nike_locale=cn/zh_cn; guidS=1bcd1dd4-5048-427d-ff6e-538557a1d424; guidU=5afdbd90-31e1-4500-b22b-52ea1ef04a61; dreams_session=catching-dreams; utag_main=_st:1418983020632$ses_id:1418982197878%3Bexp-session; APID=3FFB20AC9405E761BB25F6A64F996FBD.sin-321-app-ap-0; NIKE_COMMERCE_LANG_LOCALE=zh_CN; NIKE_COMMERCE_COUNTRY=CN; CONSUMERCHOICE=CN/zh_CN; CONSUMERCHOICE_SESSION=t; NIKE_CCR=11|CN|CN|CN|F|null|2|zh_CN|K|F; CART_SUMMARY="{\"profileId\" :\"12474976224\",\"userType\" :\"DEFAULT_USER\",\"securityStatus\" :\"0\",\"cartCount\" :0}"; mt.v=2.1199524350.1418981223023; cartSummary=0%24%24undefined%24%240%24%2412474976224%24%240%24%24undefined%24%24DEFAULT_USER%24%240%24%24undefined; pr_data=0; m_hb=1; RT=dm=nike.com&si=6363db72-c08f-4174-8464-4bb449df129f&ss=1418973255489&sl=10&tt=111424&obo=1&bcn=%2F%2F36f1f2cc.mpstat.us%2F&nu=&cl=1418981227035; s_pers=%20s_fid%3D368C659054F6A7C4-08DD9FFC923C01D9%7C1482139629265%3B%20c5%3Dnikecom%253Ecart%253Eadd%2520to%2520cart%7C1418983029268%3B%20c6%3Dcart%7C1418983029273%3B; s_sess=%20s_cc%3Dtrue%3B%20c51%3Dhorizontal%3B%20v41%3Ddirect%2520entry%3B%20s_sq%3D%3B; ResonanceSegment=1; RES_SESSIONID=575157445389777'
    print analysis_cookie(cookie)