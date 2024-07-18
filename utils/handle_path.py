# -*- coding: utf-8 -*-
# @File    : handle_path.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import os

# 当前文件路径
# print(__file__)
# #2.上一层目录
# print(os.path.dirname(__file__))
# #2.上上一层目录
# print(os.path.dirname(os.path.dirname(__file__)))
# os.path.abspath   获取完整路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('工程路径--->', project_path)
# 3.配置文件路径
config_path = os.path.join(project_path, 'configs')
# 4.
data_path = os.path.join(project_path, 'data')
report_path = os.path.join(project_path, r'outFiles\report\temp')
print(report_path)
log_path = os.path.join(project_path, r'outFiles\logs')
print(log_path)
