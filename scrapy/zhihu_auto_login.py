# -*- coding: utf-8-*-

from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()
user = '18673136299'
pwd = 'nietaihou2018'
try:
    client.login(user, pwd)
    print(u"无验证码登陆成功!")
except NeedCaptchaException:  # 处理要验证码的情况
    #  保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login(user, pwd, captcha)
    print(u"有验证码登陆成功!")
    client.save_token('token.pkl')  # 保存token
