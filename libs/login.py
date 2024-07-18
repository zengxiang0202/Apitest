# -*- coding: utf-8 -*-
# @File    : login.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
from common.baseAPI import BaseAPI
from utils.handle_data import get_md5_data
from utils.tool import show_time

"""
登录接口的特性：
    - 1.自身实现接口自动化测试
    - 2.获取身份的鉴权，给后续接口关联token
总结：登录接口有双重功能
解决方案：当一个函数需要2个不同的结果
"""


class Login(BaseAPI):  # 登录模块的 业务类名--使用这个类名去获取yml里面对应接口详情
    @show_time  # 增加计时功能
    def login(self, in_data, get_token=False):  # 登录接口
        in_data['password'] = get_md5_data(in_data['password'])
        payload = in_data
        resp = self.request_send(data=payload)  # 发送请求
        if get_token:  # 为真，需要返回token
            return resp['data']['token']
        return resp  # 接口的响应数据

# if __name__ == '__main__':#
#     login_data = {'username': 'zxy0202', 'password': 'zxy153'}
#     res = Login().login(login_data)
#     print('响应数据--->',res)
