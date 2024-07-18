# -*- coding: utf-8 -*-
# @File    : handle_yml.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import yaml


def get_yml_data(file_path: str):
    # 1.需要打开yml
    with open(file_path, encoding='utf-8') as fo:  # file object
        # 1.使用fo.read()  先读取文件内容为字符串格式
        # 2.使用yaml.safe_load()，把字符串内容变成对应的格式
        return yaml.safe_load(fo.read())


def get_yml_case(file_path: str):
    res_list = []  # 存结果数据
    # 1.直接调用获取数据的函数
    res = get_yml_data(file_path)
    # 2.数据格式[(),()]
    for one in res:
        res_list.append((one['detail'], one['data'], one['resp']))
    return res_list

# if __name__ == '__main__':
#     # res = get_yml_data('../configs/apiPathConfig.yml')
#     # print(res)
#     res = get_yml_case('../data/loginCase.yml')
#     print(res)
