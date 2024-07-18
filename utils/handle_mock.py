# -*- coding: utf-8 -*-
# @File    : handle_mock.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import requests

HOST = 'http://127.0.0.1:9999'


# def test():
#     url = f'{HOST}/xt'
#     payload = {"key1":"abc123"}
#     resp = requests.post(url,json=payload)
#
#     print(resp.text)#响应数据--字符串类型的
# if __name__ == '__main__':
#     test()

# -----------------------------申请接口请求----------------
def commit_order(in_data):
    url = f'{HOST}/api/order/create/'
    payload = in_data
    resp = requests.post(url, json=payload)
    return resp.json()


# ------------------------查询结果---------------------
"""
问题：调用几次，什么时候调用？
解决：循环要有，怎么循环
思考：
    - 1.使用什么数据去查询？----order_id
    - 2.查询要频率  多久查一次  interal 单位是s
    - 3.如果一直没有结果，是否要考虑结束！  timeout  超时
    - 4.查询时间是30s ，如果在10s就查到了，后续需要查询码？可以提早结束！
"""
import time


def get_order_result(in_id, interal=5, timeout=30):
    """
    :param in_id:
    :param interal: 频率 单位是s
    :param timeout: 超时 单位是s
    :return:
    """
    url = f'{HOST}/api/order/get_result01/'
    payload = {'order_id': in_id}
    start_time = time.time()  # 开始时间
    end_time = start_time + timeout  # 结束时间
    cnt = 1  # 查询的初始值
    while time.time() < end_time:
        resp = requests.get(url, params=payload)
        if resp.text:  # 返回是有，是正确的
            print('查询的结果是--->', resp.text)
            return  # 直接结束函数！

        else:
            print(f'---第{cnt}次*查询暂时没有结果，请稍微继续查询---')
        time.sleep(interal)  # 间隔--频率 s
        cnt += 1
    print('查询超时，请联系平台管理员！')


import threading

if __name__ == '__main__':
    start_time = time.time()  # 整个i项目自动化测试开始时间
    # ----------新增需求的自动化测试-------------------
    commit_data = {
        "user_id": "sq123456",
        "goods_id": "20200815",
        "num": 1,
        "amount": 200.6
    }
    order_id = commit_order(commit_data)['order_id']
    print('申请的id--->', order_id)
    # 2.查询
    # get_order_result(order_id)
    # --------------------------------------
    # 1.创建子线程  t1
    # target= 写对应你需要执行子线程的函数名
    # args  函数传递的参数
    t1 = threading.Thread(target=get_order_result, args=(order_id,))
    # 2.如果主线程，整个自动化测试都运行结果，子线程直接结束---守护模式
    t1.setDaemon(True)
    t1.start()
    # --------------------------------------
    # --------店铺，登录，食品 其他的业务模块自动化测试-------
    for one in range(40):
        print(f'{one}----正在执行其他业务自动化测试----')
        time.sleep(1)

    end_time = time.time()  # 自动化执行完成的时间
    print(f'项目接口自动化测试耗时--->{end_time - start_time}s')

"""
代码的编写阶段：
    1.逻辑功能实现
    2.优化阶段
    3.维护阶段
汇报：
    领导建议：功能是可以实现，但是效率是否可以提升下
分析：
    1- 执行效率低，只是一个现象
    2- 慢的原因：time.sleep(5)---中间执行机器是空闲等待的
解决：
   1- sleep是需要的
   2- 是否可以在它等待的5s 我可以干点其他事情
   3- 分析cpu：
        - cpu运算型
        - io阻塞型 
            - time.sleep()
            - requests
    4-提供效率
        1- 多线程：一个进程里的线程是共享整个进程的资源的！，在使用一个cpu的核
            多线程一定可以提供效率---不一定！
            比如：密集型运算，单线程比多线程更快
        2- 多进程：使用多个核
        3- 协程：更小单元的线程   locust就是使用协程
        4- 多进程+协程：使用多个核，一个核使用到位
实现：
    其他业务自动化测为---主线程
    订单业务--子线程
扩展：pytest自带分布式
    1- pytest-parallel 实现多线程运行测试用例
    2- 多进程运行模式 pytest-xdist
    
"""
