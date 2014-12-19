# -*-coding: utf-8 -*-
__author__ = 'Yun'
import httplib2
from urllib import urlencode


def login_nike():
    conn = httplib2.Http()
    data = dict(login="327752822@qq.com", rememberMe=True, password="Bo89989136")

    login_resp, login_content = conn.request("https://www.nike.com/profile/login?Content-Locale=zh_CN", 'POST',
                                             urlencode(data),
                                             headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return login_resp['set-cookie']




