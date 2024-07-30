# -*- coding: utf-8 -*-
# @File    : send_qiyeweixin
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/30
import os
import requests
from jenkins import Jenkins

jenkins_url = "http://192.168.21.128:8080/"
server = Jenkins(jenkins_url, username='admin', password='zxy15381272772')
job_name = "job/deliveryApitest"
job_url = server.get_info(job_name)['url']
job_last_number = server.get_info(job_name)['lastBuild']['number']
report_url = job_url + str(job_last_number) + '/allure'


def push_message():
    content = {}
    file_path = os.path.dirname(os.getcwd()) + '/allure-report/export/prometheusData.txt'
    f = open(file_path)
    for line in f.readlines():
        launch_name = line.strip('\n').split(' ')[0]
        num = line.strip('\n').split(' ')[1]
        content.update({launch_name: num})
    f.close()
    print(content)
    passed_num = content['launch_status_passed']  # 通过数量
    failed_num = content['launch_status_failed']  # 失败数量
    broken_num = content['launch_status_broken']  # 阻塞数量
    skipped_num = content['launch_status_skipped']  # 跳过数量
    case_num = content['launch_retries_run']  # 总数量
    """
    企业微信消息发送，通过webhook发送消息
    """
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=060f7e39-894b-42d3-b4d0-73f315ad0a85"
    content = {
        "msgtype": "text",
        "text": {
            "content": "接口自动化脚本执行结果：\n运行总数" + case_num
                       + "\n通过数量：" + passed_num
                       + "\n失败数量：" + failed_num
                       + "\n阻塞数量：" + broken_num
                       + "\n跳过数量：" + skipped_num
                       + "\n构建地址：\n" + job_url
                       + "\n报告地址：" + report_url
        }
    }
    requests.post(url=webhook, json=content, verify=False)


push_message()