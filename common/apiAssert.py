# -*- coding: utf-8 -*-
# @File    : apiAssert.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
print()
"""
断言：
    - 概念：
        -比较预期与实际响应是否一致，数据是否正确
    - 方式：
        1- 某些关键信息是否  ==  
        2- 增加数据 a数据，接口的响应是所有数据的返回
            in 
    - 对断言进行异常处理--日志
"""
from utils.handle_loguru import log
import traceback


class ApiAssert:
    @classmethod  # 类方法--不需要创建实例
    def api_assert(cls, result, condition, exp_result, assert_info, msg='断言操作'):
        """
        :param result: 实际接口返回响应数据
        :param condition: 断言的关系  in   ==  not in
        :param exp_result: 预期的数据
        :param assert_info:  断言关键内容
        :param msg: 描述
        :return: 暂定
        """
        try:
            # 定义下断言的类型--
            if isinstance(result[assert_info], int):  # 如果返回的结果是数字（支持绝对值方法），assert_type就只有==的情况
                assert_type = {'==': result[assert_info] == exp_result[assert_info]}
            else:
                assert_type = {
                    '==': result[assert_info] == exp_result[assert_info],
                    'in': result[assert_info] in exp_result[assert_info] if isinstance(exp_result[assert_info],
                                                                                       list) else False
                    # if isinstance()
                }
            # 如果用户输入的断言类型有的话
            if condition in assert_type:
                # 执行断言
                assert assert_type[condition]
            else:
                # 人为抛出异常
                raise AssertionError(f'使用的{condition}断言类型不存在,请输入正确的断言方式！')
            # 把断言的结果也加入日志----前面代码都没有问题才会执行这个log.info
            # 登录接口断言：断言类型：xxx,断言结果是:xx,预期的结果：xxx,实际的结果:xxx
            log.info(
                f'{msg}:断言类型:{condition},断言结果是:{assert_type[condition]},预期的结果:{exp_result[assert_info]},实际的结果:{result[assert_info]}')
        except Exception as error_object:  # 断言错误！
            log.error(traceback.format_exc())
            # 如果接口报错，是否需要通知pytest
            raise error_object
