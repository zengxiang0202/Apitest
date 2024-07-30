# -*- coding: utf-8 -*-
# @File    : test_shop.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import pytest
import os
import allure

from common.apiAssert import ApiAssert
from libs.shop import Shop
from utils.handle_excel_V4 import get_excel_data
from utils.handle_path import report_path, data_path


@allure.epic('订餐系统')
@allure.feature('店铺模块')
# 测试类打上标签 mark
@pytest.mark.shop
# condition=True  为真，或者写一个bool表达式，结果是T /F，直接跳过下面的代码

# @pytest.mark.skipif(login_status==False,reason='不运行的原因是--->,没有登录成功')
class TestShop:
    @pytest.mark.parametrize('title,req_body,exp_data',
                             get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @allure.story('查询接口')
    @allure.title('{title}')  # 用例标题
    @pytest.mark.shop_query
    def test_shop_query(self, shop_init, title, req_body, exp_data):
        res = shop_init.query(req_body)
        try:
            if res['status'] == 500:  # 用例中服务器异常的情况
                ApiAssert.api_assert(res, '==', exp_data, assert_info='error', msg='查询接口断言')
        except:
            ApiAssert.api_assert(res, '==', exp_data, assert_info='code', msg='店铺查询接口断言')
        # assert res['code'] == exp_data['code']

    @pytest.mark.parametrize('title,req_body,exp_data',
                             get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数',
                                            '响应预期结果'))
    @allure.story('更新接口')
    @allure.title('{title}')  # 用例标题
    @pytest.mark.shop_update
    # 强行跳过，但是报告里有描述我跳过不执行的原因
    # @pytest.mark.skip(reason='店铺编辑接口没有开发完成！')
    # 有没有一种跳过，是可以根据条件判断的

    def test_shop_update(self, shop_init, title, req_body, exp_data):
        with allure.step('1.用户登录+店铺创建实例'):
            pass
        with allure.step('2.获取店铺的id'):
            shop_id = shop_init.query({'page': 1, 'limit': 20})['data']['records'][0]['id']
        with allure.step('3.获取图片信息'):
            image_info = shop_init.file_upload(os.path.join(data_path, '456.png'))['data']['realFileName']
        with allure.step('4.更新接口'):
            res = shop_init.update(shop_id, image_info, req_body)
        with allure.step('5.断言'):
            ApiAssert.api_assert(res, '==', exp_data, assert_info='code', msg='店铺更新接口断言')
            # assert res['code'] == exp_data['code']


if __name__ == '__main__':
    pytest.main([__file__,'-s','--alluredir',f'{report_path}'])
    # 用mark标签定制化执行，比如只跑shop_query
    # pytest.main(["test_shop.py", "-s", "-m=shop_query", "--alluredir", report_path])
    os.system(f'allure serve "{report_path}"')

"""
关于执行的困惑点：使用定制化执行 -m -v -k 跟 skip有什么区别？
解惑：
    - 1. -m -v -k 模式，在报告里没有任何体现，领导看报告的时候。他以为你没有执行做这些接口自动化测试
    - 2.报告有这些接口，而且为什么不执行还有原因
"""

"""
当前自动化方案：
    - 直接运行自动化测试，中间哪怕有什么项目不能访问的你都会有运行所有的用例！
完善的方案：
    - 1.环境检查  check_list-----状态
        - 运行环境
        - 系统环境
        - 库环境
    - 2.满足条件才执行后面的接口自动化测试
    - 3.后续环境归位操作---可选择-不做/做
"""
