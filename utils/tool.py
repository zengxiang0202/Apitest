# -*- coding: utf-8 -*-
# @File    : tool.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
pass
"""
装饰器：目前我们的理解：在已有的代码上增加新功能，不修改原函数代码！
"""

"""
v1.0版本自动化接口测试代码写好了
"""
import time

# def test():
#     print('---接口自动化测试开始运行---')
#     time.sleep(1)
#     print('---接口自动化测试运行完成---')

# -给领导去演示，接口自动化测试运行效果-
# 领导的新需求：能不能计算出每一个自动化接口的运行时间

# ----------方案1:------------------------
# def test():
#     start_time = time.time()
#     print('---接口自动化测试开始运行---')
#     time.sleep(1)
#     print('---接口自动化测试运行完成---')
#     end_time = time.time()
#     print(f'自动化运行耗时--->{end_time-start_time}s')

"""
测试反馈：
    1- 每一个自动化测试方法都得修改代码
    2- 如果有新需求，你还得继续每一个方法都加
"""
# ----------方案2:------------------------
"""
优化思路：
    1- 不能去修改原函数代码
    2- 新的需求不就得重新写一个函数！
"""
# def test():
#     print('---接口自动化测试开始运行---')
#     time.sleep(1)
#     print('---接口自动化测试运行完成---')
#
# #新增的功能函数
# def show_time(func):
#     start_time = time.time()
#     func()#执行自动化测试
#     end_time = time.time()
#     print(f'自动化运行耗时--->{end_time-start_time}s')
#
# show_time(test)

"""
测试反馈：
    1- 原代码是没有改动的
    2- 你改变了函数的执行方式
"""
# ----------方案3:------------------------
"""
真正的需求点：
    1.新增函数的新功能；
        - 不能修改原代码
        - 不能改变代码的执行方式
解决：
    1.问同事
    2.百度
方案：python装饰器
    1.什么是装饰器？
        - 闭包
            函数里面定义函数，内函数使用了外函数的变量，外函数返回值是内函数对象
        - 装包
            函数的定义  *args  **kwargs
        - 解包
            函数调用： *[100,200]  **{"a":100}
    2.装饰器怎么使用？
        更加简单方便的用法：语法糖 @
"""


# 新增的功能函数
def show_time(func):  # 外函数
    def inner(*args, **kwargs):  # 内函数
        start_time = time.time()
        res = func(*args, **kwargs)  # 执行自动化测试# res=login()
        end_time = time.time()
        print(f'自动化运行耗时--->{end_time - start_time}s')
        return res

    return inner


@show_time  # test=show_time(test)
def test():
    print('---接口自动化测试开始运行---')
    time.sleep(1)
    print('---接口自动化测试运行完成---')


"""




"""
if __name__ == '__main__':
    # 把自动化测试的函数，直接传递给新增功能函数！
    # test = show_time(test)# inner函数对象   test = inner
    test()  # inner()
