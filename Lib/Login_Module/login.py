# -*- coding: utf-8 -*-
# @File : login.py
# _author_=feng
# date: 2021/1/13
import requests
import json
from ...configs.config import HOST


class Login_TP:
    # def __init__(self, s):
    #     self.s = s
    def api_login(self, inData):
        login_url = f'{HOST}api/v1/sys/oauth/token'
        # 1.构造请求消息体
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic emhhbmppYW5nLXNzby10ZXN0OmFhYTQ0ZjI3LTc0MmYtNDMzMS05ZTA0LTllMDFmMGE1MmVjNg=='}
        # 2.构造请求消息体
        payload = inData  # 下面函数直接把inData参数写到requests请求中了
        # 读的Excel表中的数据需要json.loads(inData)（因为表中读出来的是字符串）
        # payload = json.loads(inData)  # inData是字符串，转字典传入
        # 3.发送Post请求
        reps = requests.post(login_url, headers=header, data=payload)
        return reps.json()  # ['token_type']

    def api_login_p(self, inData):
        login_url = f'{HOST}api/v1/sys/oauth/token'
        # 1.构造请求消息体
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic emhhbmppYW5nLXNzby10ZXN0OmFhYTQ0ZjI3LTc0MmYtNDMzMS05ZTA0LTllMDFmMGE1MmVjNg=='}
        # 2.构造请求消息体
        # payload = json.loads(inData)  # inData是字符串，转字典传入
        # 3.发送Post请求
        reps = requests.post(login_url, headers=header, data=inData)
        return reps.json()['msg']

    def api_login_u(self, inData):
        login_url = f'{HOST}api/v1/sys/oauth/token'
        # 1.构造请求消息体
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic emhhbmppYW5nLXNzby10ZXN0OmFhYTQ0ZjI3LTc0MmYtNDMzMS05ZTA0LTllMDFmMGE1MmVjNg=='}
        # 2.构造请求消息体
        # payload = json.loads(inData)  # inData是字符串，转字典传入
        # 3.发送Post请求
        reps = requests.post(login_url, headers=header, data=inData)
        return reps.json()['msg']

# if __name__ == '__main__':
#       a = Login_TP().api_login()
#       print(a.text)
#       # LoginClass().api_login(get_excelData('1登录模块', 2, 2)
