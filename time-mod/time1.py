#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __Author__=neonie
import time
from time import gmtime, strftime

t = time.localtime()
print(time.asctime(t))
print(strftime("%a,%d %b %Y %H:%M:%S +0000", gmtime()))
print(strftime("%a,%d %b %Y %H:%M:%S +0000", gmtime(1234567890)))
print(strftime("%A",gmtime()))
print(strftime("%D",gmtime()))
print(strftime("%B",gmtime()))
print(strftime("%y",gmtime()))
# 以毫秒为单位获取当前时间
milliseconds=int(round(time.time()*1000))
print(milliseconds)