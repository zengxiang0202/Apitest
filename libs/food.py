# -*- coding: utf-8 -*-
# @File    : food.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/19
import json
# -*- coding: utf-8 -*-
# @File    : food.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
from common.baseAPI import BaseAPI


class Food(BaseAPI):  # 店铺模块的 业务类名--使用这个类名去获取yml里面对应接口详情
    # 1.添加食品种类 -- 可以不写，直接用基类的add方法即可
    def addcategory(self, shop_id, in_data):
        if in_data['restaurant_id'] == '${id}':
            in_data['restaurant_id'] = shop_id
        return super(Food, self).request_send(data=in_data)

    # 2.添加食品
    def addfood(self, in_data):
        if in_data['attributesJson']:
            in_data['attributesJson'] = json.dumps(in_data['attributesJson']).encode('utf-8').decode('unicode_escape')
        if in_data['specsJson']:
            in_data['specsJson'] = json.dumps(in_data['specsJson']).encode('utf-8').decode('unicode_escape')
        return super(Food, self).request_send(data=in_data)

    # 3.列出食品 --可以不写，直接使用父类方法

    # 4.编辑食品
    def update(self, in_data):
        if in_data['specsJson']:
            in_data['specsJson'] = json.dumps(in_data['specsJson']).encode('utf-8').decode('unicode_escape')
        return super(Food, self).update(data=in_data)
    # 5.删除食品 --可以不写，直接使用父类方法
