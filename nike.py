# -*- coding:utf-8 -*-
__author__ = 'Yun'
from urllib import urlencode
import httplib2
import json
import wx


class Login(wx.Frame):
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.Center()  # 窗口位置居中

        self.panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.name_box = wx.BoxSizer(wx.HORIZONTAL)
        self.pwd_box = wx.BoxSizer(wx.HORIZONTAL)

        self.name_label = wx.StaticText(self.panel, -1, label=u"登录名:", pos=(20, 20), size=(50, 20))
        self.name_text = wx.TextCtrl(self.panel, -1, pos=(80, 20), size=(150, 20))
        self.name_box.Add(self.name_label, 0, wx.EXPAND)
        self.name_box.Add(self.name_text, 0, wx.EXPAND)

        self.pwd_label = wx.StaticText(self.panel, -1, label=u"密码:", pos=(20, 60), size=(50, 20))
        self.pwd_text = wx.TextCtrl(self.panel, -1, pos=(80, 60), size=(150, 20), style=wx.TE_PASSWORD)
        self.pwd_box.Add(self.pwd_label, 0, wx.EXPAND)
        self.pwd_box.Add(self.pwd_text, 0, wx.EXPAND)

        self.login_btn = wx.Button(self.panel, -1, label=u"登录", pos=(50, 80), size=(50, 20))

        self.vbox.Add(self.name_box, 0, wx.EXPAND)
        self.vbox.Add(self.pwd_box, 0, wx.EXPAND)
        self.vbox.Add(self.login_btn)
        self.panel.SetSizer(self.vbox)
        self.Show()

        self.Bind(wx.EVT_BUTTON, self.login, self.login_btn)

    def login(self, e):
        username = self.name_text.GetValue()
        password = self.pwd_text.GetValue()
        if username != '' or password != '':
            conn = httplib2.Http()
            data = dict(login=username, rememberMe=True, password=password)
            print(urlencode(data))
            resp, content = conn.request("https://www.nike.com/profile/login?Content-Locale=zh_CN", 'POST',
                                         urlencode(data),
                                         headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print resp, content
            content = json.loads(content)
            if int(resp['status']) == 200:
                self.Hide()
                m = Main(self, u'{0}({1})'.format(content['entity']['screenName'], content['entity']['id']), (400, 250),
                         {"message": content})
                m.Show()
            else:
                dil = wx.MessageDialog(None, u'登录失败，用户名或密码错误！', u'消息', wx.OK)
                dil.SetOKLabel(u'确定')
                dil.ShowModal()
        else:
            dil = wx.MessageDialog(None, u'登录名或密码不能为空！', u'消息', wx.OK)
            dil.SetOKLabel(u'确定')
            dil.ShowModal()


class Main(wx.Frame):
    def __init__(self, parent, title, size, message):
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.message = message
        self.Center()
        print(message)
        self.Bind(wx.EVT_CLOSE, self.exit)
        self.main_panel = wx.Panel(self)
        self.id_label = wx.StaticText(self.main_panel, -1, label=u'产品ID:', pos=(20, 20), size=(50, 25))
        self.id_text = wx.TextCtrl(self.main_panel, -1, pos=(70, 17), size=(75, 25))
        self.price_label = wx.StaticText(self.main_panel, -1, label=u'价格:', pos=(180, 20), size=(30, 25))
        self.price_text = wx.TextCtrl(self.main_panel, -1, pos=(215, 17), size=(75, 25))



    def exit(self, event):
        self.Destroy()


default_query_params = {
    u"callback": u"nike_Cart_hanleJCartResponse",
    u"action": u"addItem",
    u"lang_locale": u"zh_CN",
    u"country": u"CN",
    u"catalogID": u"4",
    u"productID": u"10188307",
    u"price": u"899.0",
    u"siteId": None,
    u"line1": u"Nike Internationalist Mid QS",
    u"line2": u"男子运动鞋",
    u"passcode": None,
    u"sizeType": None,
    u"skuAndSize": u"11379175:42",
    u"qty": u"1",
    u"rt": u"json",
    u"view": u"3",
    u"skuId": u"11379175",
    u"displaySize": u"42",
    u"_": u"1418695131412"
}