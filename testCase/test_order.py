# -*- coding: utf-8 -*-
# @File    : test_order.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import pytest
import allure
import os

from common.apiAssert import ApiAssert
from utils.handle_excel_V4 import get_excel_data
from utils.handle_path import report_path


@allure.epic('订餐系统')
@allure.feature('订单模块')

class TestMyOrder:
    @pytest.mark.parametrize('title,req_body,exp_data',
                             get_excel_data('我的订单', 'searchorder', '标题', '请求参数',
                                            '响应预期结果'))
    @allure.story('订单搜索接口')
    @allure.title('{title}')  # 用例标题
    def test_order_search(self,order_init, title,req_body,exp_data):
        res = order_init.query(req_body)
        if 'error' in list(res.keys()):
            ApiAssert.api_assert(res,'==',exp_data,assert_info='error',msg='订单搜索接口')
        else:
            ApiAssert.api_assert(res,'==',exp_data,assert_info='code',msg='订单搜索接口')

if __name__ == '__main__':
    pytest.main([__file__, '-sv', '--alluredir', f'{report_path}'])
    # os.system(f'allure generate "{report_path}" -o "{report_path}/html"') 这句就是会在指定的report里面在生成一份html文件。
    os.system(f'allure serve "{report_path}"')