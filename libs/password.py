# -*- coding: utf-8 -*-
# @File    : password.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
from common.baseAPI import BaseAPI
from utils.handle_data import get_md5_data


class UpdatePwd(BaseAPI):
    def update(self,in_data):
        in_data['oldPassword'] = get_md5_data(in_data['oldPassword'])
        in_data['password'] = get_md5_data(in_data['password'])
        in_data['rePassword'] = get_md5_data(in_data['rePassword'])
        return super().update(data=in_data)
    def logout(self):
        return super(UpdatePwd, self).request_send()