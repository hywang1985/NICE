# -*-coding: utf-8 -*-
__author__ = 'Yun'
import httplib2
from urllib import urlencode

conn = httplib2.Http()
data = dict(login=u"327752822@qq.com", rememberMe=True, password=u"Bo89989136")
print urlencode(data)

resp, content = conn.request("https://www.nike.com/profile/login?Content-Locale=zh_CN", 'POST', urlencode(data),
                             headers={'Content-Type': 'application/x-www-form-urlencoded'})

print resp, content
