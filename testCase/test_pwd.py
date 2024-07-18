# -*- coding: utf-8 -*-
# @File    : test_order.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import allure
import pytest

from common.apiAssert import ApiAssert
from utils.handle_excel_V4 import get_excel_data


@allure.epic('订餐系统')
@allure.feature('密码模块')

class TestMyOrder:
    @pytest.mark.parametrize('title,req_body,exp_data',
                             get_excel_data('修改密码', 'update', '标题', '请求参数',
                                            '响应预期结果'))
    @allure.story('修改密码接口')
    @allure.title('{title}')  # 用例标题
    def test_update_pwd(self,update_pwd_init, title,req_body,exp_data):
        res = update_pwd_init.update(req_body)
        ApiAssert.api_assert(res,'==',exp_data,assert_info='code',msg='修改密码接口')

    @pytest.mark.parametrize('title,req_body,exp_data',
                             get_excel_data('修改密码', 'logout', '标题', '请求参数',
                                            '响应预期结果'))
    @allure.story('退出登录接口')
    @allure.title('{title}')  # 用例标题
    def test_logout(self, update_pwd_init, title, req_body, exp_data):
        res = update_pwd_init.logout()
        ApiAssert.api_assert(res, '==', exp_data, assert_info='code', msg='退出登录接口')

if __name__ == '__main__':
    pytest.main([__file__,'-sv'])