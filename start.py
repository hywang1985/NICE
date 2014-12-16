# -*-coding:utf-8 -*-
__author__ = 'Yun'
from nike import Login, Main
import httplib2
import json
import wx


app = wx.App(False)

win_size = (300, 200)
main_win_size = (500, 300)

application = Main(None, "Nike", main_win_size, {'message': 'message'})
application.Show()
app.MainLoop()