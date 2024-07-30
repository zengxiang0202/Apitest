# -*- coding: utf-8 -*-
# @File    : test_login.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
from libs.login import Login
from utils.handle_excel_V4 import get_excel_data
import pytest
import os
from utils.handle_path import report_path, data_path
import allure
from common.apiAssert import ApiAssert


@allure.epic('订餐系统')
@allure.feature('登录模块')
# 1.测试类
class TestLogin:
    # 2.测试方法
    @pytest.mark.parametrize('title,req_body,exp_data',
                             get_excel_data('登录模块', 'Login', '标题', '请求参数', '响应预期结果'))
    @allure.story('登录接口')
    @allure.title('{title}')  # 用例标题
    def test_login(self, title, req_body, exp_data):  # 跑接口--用例  data driver testing
        # 1.需要调用接口发送
        res = Login().login(req_body)
        # 2.做断言  实际数据与预期的结果比较,找关键数据或者标志数据对比
        ApiAssert.api_assert(res, '==', exp_data, assert_info='msg', msg='登录接口断言')


if __name__ == '__main__':
    # '-s' 打印print内容
    pytest.main([__file__, '-s', '--alluredir', f'{report_path}'])
    #   添加 --clean-alluredir 参数会在生成新的 Allure 报告之前清空指定的目录。这样每次运行测试时，报告目录会被清空，
    #   以确保报告中只包含当前运行测试的结果，而不会混杂之前运行的结果。有助于确保报告的准确性和清晰度。
    os.system(f'allure serve "{report_path}"')
    # 报告：方案：allure
    """
    报告的运行原理：
        1- 使用pytest生成需要的源数据   --alluredir 存放json文件
        2- 使用allure 去读取这些数据产生报告
    """
