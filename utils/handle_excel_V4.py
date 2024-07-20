# -*- coding: utf-8 -*-
# @File    : handle_excel_V4.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
pass
"""
优化需求：用例筛选，定制化执行
需求分析：
    - 单选某一个： tc001
    - 连续几个： tc003-tc006
    - 混合的筛选： tc002, tc007-tc009
    - 全部运行 all

"""
# xlutils  写入excel文件 worksheet.write(行号，列号，内容)
import xlrd  # pip install xlrd#   panda  openpyxl
import json
from utils.handle_yml import get_yml_data
from utils.handle_path import config_path, data_path
import os


def get_excel_data(sheet_name, case_name, *args, run_case=['all']):
    # 1.打开文件-从文件路径读取到内存

    # excel文件名：file_name == Delivery_System_V1.5.xls
    file_name = get_yml_data(os.path.join(config_path, 'caseConfig.yml'))['file_name']
    # 拼接excel文件路径
    file_path = os.path.join(data_path, file_name)

    # formatting_info=True 保证excel文件原样式
    work_book = xlrd.open_workbook(file_path, formatting_info=True)

    # 2.获取sheet对象
    work_sheet = work_book.sheet_by_name(sheet_name)

    # #扩展1：获取一行数据
    # print(work_sheet.row_values(0))
    # #扩展2：获取一列数据
    # print(work_sheet.col_values(0))
    # #扩展3：获取单元格数据 坐标（行编号，列编号）
    # print(work_sheet.cell(0,0).value)
    col_indexs = []  # 表头数据
    for one in args:
        # 列表的元素的下标怎么求  列表.index(元素)
        # [7,9]
        col_indexs.append(work_sheet.row_values(0).index(one))  # 0行数据--列表  7
    # print('用户输入的表头对应的列编号是>>>',col_indexs)

    # -------------------------用例筛选-----------------------------
    # 示例 run_case= ['all','001','003-006','009']
    run_list = []  # 最后存放的结果！
    # 1.判断
    if 'all' in run_case:  # 直接全部运行
        run_list = work_sheet.col_values(0)  # Login001
    else:  # 不是运行所有的
        for one in run_case:
            # 如果是连续，去处理
            if '-' in one:  # '003-006'
                start, end = one.split('-')  # 003'  006  字符串类型
                for i in range(int(start), int(end) + 1):  # 3 4 5 6
                    # Login+003--->Login003
                    run_list.append(f'{case_name}{i:0>3}')  # [3,4,5,6]
            else:  # 说明是单个用例
                run_list.append(f'{case_name}{one:>3}')  # [3,4,5,6]

    # print('用户筛选出来执行的用例编号是>>>',run_list)

    # 3.获取对应的数据
    row_index = 0  # 初始行编号
    res_data = []  # 结果返回数据
    for one in work_sheet.col_values(0):  # 根据第0列数据的个数进行遍历次数
        if case_name in one and one in run_list:  # 'Login' in ‘Login001’
            col_data = []  # 一行所有需要获取的列数据
            for col in col_indexs:  # [,5,7,9]
                tmp = is_json(work_sheet.cell(row_index, col).value)  # i请求数据
                col_data.append(tmp)

            # [(请求数据1，响应数据1),(请求数据2，响应数据2)]
            res_data.append(tuple(col_data))
        row_index += 1  # 下一行
    return res_data


# -------------------判断是否是json格式的函数----------
# 如果是json--返回字典给我，不是json  直接原样返回
def is_json(in_str):
    try:
        return json.loads(in_str)  # 如果转化可以成功，说明就是json
    except:
        return in_str


# if __name__ == '__main__':
#     res = get_excel_data('登录模块','Login',run_case=['001','003-004','005'])
#     for one in res:
#         print(one)

"""

    1- 把参数做成配置文件yml  试了下login.yml
    2- 可以做一个简易的交互操作  gui/web页面
"""
