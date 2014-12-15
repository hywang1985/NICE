# -*-coding:utf-8 -*-
__author__ = 'Yun'
from nike import Login
import httplib2
import json
import wx


app = wx.App(False)

win_size = (300, 200)

application = Login(None, "Nike", win_size)
app.MainLoop()