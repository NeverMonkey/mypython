#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-15 13:58:48
# @Author  : taihou.nie (nevermonkey@126.com)
# @Link    : https://github.com/NeverMonkey
# @Host    : HP


try:
line = [name] + load_lianjia_detail_page(href)
if print_progress:
    print('1:', ','.join(line))
except Exception as e:
if 'HTTP Error 404' in traceback.format_exc():  # 无子页面
line = [name] + load_lianjia_main_page_item(li, title)
if print_progress:
    print('2:', ','.join(line))
else:
print("Error at loading:", title)
traceback.print_exc()
continue
