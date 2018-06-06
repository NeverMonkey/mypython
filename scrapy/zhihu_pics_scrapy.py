#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import time
import os
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException


def auto_login(user, pwd):
    client = ZhihuClient()
    try:
        client.login(user, pwd)
        print(u"无验证码登陆成功!")
    except NeedCaptchaException:  # 处理要验证码的情况
        #  保存验证码并提示输入，重新登录
        with open('auth.gif', 'wb') as f:
            f.write(client.get_captcha())
        captcha = input('please input captcha:')
        client.login(user, pwd, captcha)
        print(u"有验证码登陆成功!")
        client.save_token('token.pkl')  # 保存token


def get_images(id):
    question = client.question(id)
    print(u"问题:", question.title)
    print(u"回答数量:", question.answer_count)
    base_dir = 'D:\\Anaconda\\Spyder\\'
    pic_path = base_dir + question.title + u"(图片)"
    # 建立存放图片的文件夹
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    index = 1  # 图片序号
    for answer in question.answers:
        content = answer.content  # 回答内容
        re_compile = re.compile(r'<img src="(https://pic\d\.zhimg\.com/.*?\.(jpg|png))".*?>')
        img_lists = re.findall(re_compile, content)
        if (img_lists):
            for img in img_lists:
                img_url = img[0]  # 图片url
                request.urlretrieve(img_url, pic_path + u"/%d.jpg" % index)
                print(u"成功保存第%d张图片" % index)
                index += 1


# def get_images(aurl):
#     html = request.urlopen(aurl).read().decode('utf-8')
#     soup = BeautifulSoup(html, 'html.parser')
#     # print(soup.prettify())
#
#     # 用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句
#     links = soup.find_all('img', "origin_image zh-lightbox-thumb", src=re.compile(r'.jpg$'))
#     print(links)
#
#     # 设置保存图片的路径，否则会保存到程序当前路径
#     dir_list = re.split(r'\/', aurl)
#     parpath = 'D:\\Anaconda\\Spyder\\'  # 路径前的r是保持字符串原始值的意思，就是说不对其中的符号进行转义
#     tarpath = parpath + '\\'.join(dir_list[2:])
#     if not os.path.exists(tarpath):
#         os.makedirs(tarpath)
#     for link in links:
#         print(link.attrs['src'])
#         # 保存链接并命名，time.time()返回当前时间戳防止命名冲突
#         request.urlretrieve(link.attrs['src'], tarpath + '\%s.jpg' % time.time())

user = '18673136299'
pwd = 'nietaihou2018'
q_list = ['22918070', '35627766', '26037846', '263470102', '34078228', '26037846', '24400664']

if __name__ == '__main__':
    # print("第一次登录认证")
    # auto_login(user, pwd)
    print("登录认证")
    client = ZhihuClient()
    client.load_token('token.pkl')
    for q_id in q_list:
        # url = 'https://www.zhihu.com/question/' + q_id
        # print("开始爬取{}".format(url))
        get_images(int(q_id))
