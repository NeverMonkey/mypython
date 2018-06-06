#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __Author__=neonie

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

url = 'http://music.163.com/#/discover/playlist/?order=hot'
# 创建一个webdriver
# 1.PhantomJS
# driver=webdriver.PhantomJS()

# 2.chrome headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

# 准备好csv文件
csv_file1 = open("playlist1.csv", "w", newline='')
csv_file2 = open("playlist2.csv", "w", newline='')
writer1 = csv.writer(csv_file1)
writer2 = csv.writer(csv_file2)
writer1.writerow(['标题', '播放数', '链接'])
writer2.writerow(['标题', '播放数', '链接'])
# 解析每一页，知道下一页为空
m_list = []
page_count = 0
while url != 'javascript:void(0)':
    # 用webdriver加载页面
    driver.get(url)
    # 切换到内容的iframe
    driver.switch_to.frame("contentFrame")
    # 定位歌单标签
    data = driver.find_element_by_id("m-pl-container").find_element_by_tag_name("li")
    print(driver.find_element_by_id("m-pl-container").find_element_by_tag_name("li"))
    m_list.append(data)
    page_count += 1
    nb = data.find_element_by_class_name("nb").text
    if '万' in nb and int(nb.split("万")[0]) > 200:
        msk = data.find_element_by_css_selector("a.msk")
        print([msk.get_attribute('title'),
               nb, msk.get_attribute('href')])
        writer1.writerow([msk.get_attribute('title'),
                          nb, msk.get_attribute('href')])

    print(" The {} page has been done".format(page_count))
    # 定位下一页的url
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')

# 解析每一页的所有歌单
# for i in range(len(m_list)):
#     # 获取播放数
#     print(m_list[i])
#     nb = m_list[i].find_element_by_class_name("nb").text
#     if '万' in nb and int(nb.split("万")[0]) > 500:
#         # 获取歌单封面
#         msk = m_list[i].find_element_by_css_selector("a.msk")
#         # 将歌单信息写入文件
#         writer2.writerow([msk.get_attribute('title'),
#                           nb, msk.get_attribute('href')])

csv_file1.close()
csv_file2.close()
