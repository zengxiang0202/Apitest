# -*- coding: utf-8 -*-
# @File    : conftest.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import pytest

from libs.food import Food
from libs.login import Login
from libs.order import MyOrder
from libs.password import UpdatePwd
from libs.shop import Shop
from configs.config import USER_INFO
from utils.handle_excel_V4 import get_excel_data
from utils.handle_path import report_path
import os

# 环境检查
"""

"""


# @pytest.fixture(scope='session', autouse=True)
# def start_running():
#     print('---清除报告的的历史数据---')
#     try:
#         for one in os.listdir(report_path):
#             if 'json' in one or 'txt' in one:
#                 os.remove(f'{report_path}/{one}')
#     except:
#         print('第一次执行pytest框架')
#     yield
#     print('自动化完成，做一些数据清除的操作')

# ----前置操作---登录操作-----
# fixture有返回值的情况下，你使用这个函数的名字，就是调用它的返回值
@pytest.fixture(scope='session')
def login_init():
    # 1.调用登录的接口，获取token
    token = Login().login(USER_INFO, get_token=True)
    yield token  # 返回这个token值#
    print('数据清除--用户退出')


"""
在项目里，如果多个fixture函数需要相互关联，
下一个fixture函数使用上一个fixture函数名就等价于使用这个函数的返回值！
"""


@pytest.fixture(scope='session')
def shop_init(login_init):
    # 1.调用创建店铺实例
    shop = Shop(login_init)
    yield shop  # 返回这个token值


# #params---fixture做参数化使用的
# params=  可以使用函数的返回值  get_excel_data()
# @pytest.fixture(scope='session',params=[100,200],autouse=True)
# def env_init(request):
#     print('新增测试数据')
#     print('fixture的参数是--->',request.param)
#     yield
#     print('删除数据，你需要怎么删除就调用具体的删除操作')

def pytest_collection_modifyitems(items):
    # 解决pytest执行用例，标题有中文时显示编码不正确的问题
    # print('items是：',items)
    for item in items:
        # print('item是：',item)
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")



"""
编码：把字符串变成计算机可以识别的字节码
解码：把计算机可以识别 的字节码，变成我们可以认识的编码

本来环境就是utf-8 ----  先使用encode('utf-8')变成 字节码---使用解码函数decode('unicode')

"""


# 初始化食品
@pytest.fixture(scope='class')
def food_init(login_init):
    food = Food(login_init)
    # food.add({"name": "%E9%A3%9F%E5%93%81%E7%A7%8D%E7%B1%BB1","description": "%E7%A7%8D%E7%B1%BB%E6%8F%8F%E8%BF%B01","restaurant_id": "12679"})
    yield food


# 初始化查询食品
@pytest.fixture(scope='class')
def query_food_init(food_init):
    query_food = food_init.query({"page": 1, "limit": 20})
    yield query_food


# 初始化订单
@pytest.fixture(scope='class')
def order_init(login_init):
    order = MyOrder(login_init)
    # title,in_data = get_excel_data('我的订单','searchorder','请求参数')
    # query_order = order.query(in_data)
    print('订单模块初始化...')
    yield order


# 初始化修改密码模块
@pytest.fixture(scope='class')
def update_pwd_init(login_init):
    pwd = UpdatePwd(login_init)
    print('修改密码模块初始化...')
    return pwd


