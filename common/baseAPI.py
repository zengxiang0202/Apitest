# -*- coding: utf-8 -*-
# @File    : baseAPI.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
import requests

"""
基类：
    - 1.里面需要写一个公共的发送方法
    - def request_send(self,method,url,data,json,params,files,)
        - 1.参数的传递问题：
         解决：
            - 1.方案1：使用可缺省参数  *args,按照顺序对号入座
            - 方案2：使用关键字参数  **kwargs，传递的使用 变量=值，写法  ***
        - 2.接口数据来说，一个接口涉及很多 100 用例
            - 1. data,json,params请求数据都是根据用例不同而不同，必须获取用例数据
            - 2.method,url 接口只要不维护，不修改接口文档，就不会改变
                - 方案1：从用例获取
                - 方案2：是否可以剥离，使用配置文件yaml
#------------------------------------------------------------
接口路径配置文件的设计模式：取决接口的风格
    - 1.常规风格，没有标准的格式，开发可以自定义
        - 举例：一个业务，不同接口url不一样
            - 增加接口：POST  路径  /add/shopping/xt
            - 编辑接口：POST  路径  /update/shopping/sq
    - 2. restful接口规范
        - 不同的接口类型，有规范的方法  查询 get  增加 post 修改 put  删除 delete
        - 所有的这个业务，接口路径是一样的



难点：具体的接口调用基类的request_send()，外卖就获取这个调用方法名字，去yml获取对应的method  path
    

"""
from utils.handle_yml import get_yml_data
import inspect
import traceback
from configs.config import HOST
from utils.handle_loguru import log
from utils.handle_path import config_path
import os


class BaseAPI:  # 基类---后续业务类需要继承这个基类
    def __init__(self, in_token=None):  # 获取每一个业务模块类的接口的路径与方法
        # -------增加请求头的鉴权---------------------
        if in_token:  # 1.业务模块需要请求头的token
            self.header = {'Authorization': in_token, }
        else:  # 2.登录模块不需要
            self.header = None
        # ------------------------------------------
        # self.data  是这个业务模块所有的数据，
        self.data = get_yml_data(os.path.join(config_path, 'apiPathConfig.yml'))[self.__class__.__name__]
        # print('继承的子类类名是>>>',self.__class__.__name__)
        # print('这个业务类的接口数据是>>>',self.data)

    def request_send(self, id='',
                     **kwargs):  # 公共方法--是给所有的请求使用 -----不能用**kwargs，是个坑，后面有的请求体是列表套字典，如果被解包就会解错，最后几个字段错了，如下：
        # 请求体数据:name=%E7%82%B8%E9%B8%A1%E6%B5%8B%E8%AF%95&idShop=12679&category_id=81190&attributesJson=%E6%96%B0&specsJson=specs&specsJson=packing_fee&specsJson=price
        # 上面的注释，说法是错的，即使不用**kwargs，也会自动解包，把excel中的字典格式变为表单
        # def request_send(self,data=None,params=None,files=None,id=''):
        # print('**在函数定义的时候的作用>>>',kwargs)
        try:
            # 获取对应接口的详情数据  method  path
            self.configData = self.data[inspect.stack()[1][3]]
            # 发送请求
            resp = requests.request(
                method=self.configData['method'],
                url=f'{HOST}{self.configData["path"]}/{id}',
                headers=self.header,
                # data=data,
                # params=params,
                # files=files)
                **kwargs)  # 需要解包 把字典--变成 变量=值写法
            # -------------------------把请求详情全部日志化---info
            log.info(f'''业务模块名:{self.__class__.__name__},接口名:{inspect.stack()[1][3]},
    请求的url:{resp.request.url},
    请求的方法:{resp.request.method},
    请求体数据:{resp.request.body},
    响应数据:{resp.json()},
    响应状态码:{resp.status_code}
''')

            return resp.json()  # 得到的是字典
        except Exception as error:
            print('公共发送方法有异常，请检查下！！！')
            print(traceback.format_exc())  # 报错信息
            # 不管请求是否报错，我都可以按照需求去打日志
            log.error(traceback.format_exc())

    # -----------------封装常用的增删改查接口方法---------------
    def query(self, in_data):  # 查询接口
        return self.request_send(params=in_data)

    def update(self, **in_data):  # 更新接口
        return self.request_send(**in_data)

    def add(self, **in_data):  # 添加接口
        return self.request_send(**in_data)

    def delete(self, id=''):  # 删除接口  id
        return self.request_send(id=id)

    # 文件上传
    # jmeter这类工具也有文件上传
    """
    传递文件接口：文件属性：文件的路径，文件名字，文件格式
    user_file = {'接收文件的变量名':(文件名，文件对象本身，文件格式)}
    用户输入的是：字符串，文件路径   d:/xt/sq.png
    """

    def file_upload(self, file_path: str):
        file_name = file_path.split('/')[-1]  # sq.png
        file_type = file_path.split('.')[-1]  # png
        user_file = {'file': (file_name, open(file_path, 'rb'), file_type)}
        return self.request_send(files=user_file)

# --------------------获取函数调用者的函数名
# import inspect#内置模块，获取函数的堆栈信息
# def test():
#     print('是谁调用了我，它的函数名是>>>',inspect.stack()[1][3])
#
# def a():
#     test()
#
# a()
