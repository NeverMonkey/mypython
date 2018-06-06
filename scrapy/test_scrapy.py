#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
wb_data = requests.get(url)
# print(wb_data)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select(
    'div.listing_info > div.listing_title > a[target="_blank"]')
imgs = soup.select('img[width="180"]')
cates = soup.select('div.tag_line > div.p13n_reasoning_v2')
# print(cates)
for title, img, cate in zip(titles, imgs, cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings),
    }
    print(data)
