# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import pytest
import os
import allure

from common.apiAssert import ApiAssert
from libs.food import Food
from utils.handle_path import report_path,data_path
from utils.handle_excel_V4 import get_excel_data

@allure.epic('订餐系统')
@allure.feature('食品模块')
class TestFood:
    @pytest.mark.parametrize('title,req_body,exp_body',get_excel_data('食品管理','Addfoodkind','标题',
                                                                      '请求参数','响应预期结果'))
    @allure.story('添加食品种类接口')
    @allure.title('{title}')
    def test_foodkind_add(self,shop_init,food_init,title,req_body,exp_body):
        #1.登录
        with allure.step('1.用户登录+食品创建实例'):
            pass
        #2.添加食品种类
        with allure.step('2.获取店铺的id'):
            shop_id = shop_init.query({'page':1,'limit':20})['data']['records'][0]['id']
        with allure.step('3.添加食品种类'):
            res = food_init.addcategory(shop_id,req_body)
        #3.断言
        with allure.step('4.断言'):
            if 'error' in list(res.keys()):
                ApiAssert.api_assert(res, '==', exp_body, assert_info='error', msg='添加食品种类接口')
            else:
                ApiAssert.api_assert(res,'==',exp_body,assert_info='code',msg='添加食品种类接口')

    @pytest.mark.parametrize('title,req_body,exp_body',get_excel_data('食品管理','Addfood','标题',
                                                                      '请求参数','响应预期结果',run_case=['010-012']))
    @allure.story('添加食品接口')
    @allure.title('{title}')
    def test_food_add(self,food_init,title,req_body,exp_body):
        # 1.登录
        with allure.step('1.用户登录+食品创建实例'):
            pass
        # 2.添加食品
        with allure.step('2.添加食品'):
            # print(req_body)
            res = food_init.addfood(req_body)
        # 3.断言
        with allure.step('3.断言'):
            if 'error' in list(res.keys()):
                ApiAssert.api_assert(res, '==', exp_body, assert_info='error', msg='添加食品接口')
            else:
                ApiAssert.api_assert(res,'==',exp_body,assert_info='code',msg='添加食品接口')

    @pytest.mark.parametrize('title,req_body,exp_body',get_excel_data('食品管理','listfood','标题',
                                                                      '请求参数','响应预期结果'))
    @allure.story('列出食品接口')
    @allure.title('{title}')
    def test_food_list(self,food_init,title,req_body,exp_body):
        res = food_init.query(req_body)
        if 'error' in list(res.keys()):
            ApiAssert.api_assert(res, '==', exp_body, assert_info='error', msg='列出食品接口')
        else:
            ApiAssert.api_assert(res,'==',exp_body,assert_info='code',msg='列出食品接口')

    @pytest.mark.parametrize('title,req_body,exp_body', get_excel_data('食品管理', 'updatefood', '标题',
                                                                       '请求参数', '响应预期结果'))
    @allure.story('编辑食品接口')
    @allure.title('{title}')
    def test_food_update(self, food_init, title, req_body, exp_body):
        res = food_init.update(req_body)
        if 'error' in list(res.keys()):
            ApiAssert.api_assert(res, '==', exp_body, assert_info='error', msg='编辑食品接口')
        else:
            ApiAssert.api_assert(res, '==', exp_body, assert_info='code', msg='编辑食品接口')

    @pytest.mark.parametrize('title,req_body,exp_body', get_excel_data('食品管理', 'deletefood', '标题',
                                                                       '请求参数', '响应预期结果'))
    @allure.story('删除食品接口')
    @allure.title('{title}')
    def test_food_delete(self, food_init, query_food_init, title, req_body, exp_body):
        if req_body['id'] == 'id':  # 如果用例中id为id，则把最新的食品id进行替换
            if query_food_init['data']['records']:  # 检查 records 列表是否非空
                req_body['id'] = query_food_init['data']['records'][-1]['item_id']
            else:
                pytest.skip("No records found in query_food_init['data']['records']")
        res = food_init.delete(req_body['id'])
        if 'error' in list(res.keys()):
            ApiAssert.api_assert(res, '==', exp_body, assert_info='error', msg='编辑食品接口')
        else:
            ApiAssert.api_assert(res, '==', exp_body, assert_info='code', msg='编辑食品接口')
if __name__ == '__main__':
    pytest.main([__file__,'-sv','--alluredir',f'{report_path}',"--clean-alluredir"])
    os.system(f'allure serve "{report_path}"')
