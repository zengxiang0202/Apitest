# -*- coding: utf-8 -*-
# @File    : shop.py
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/16
from common.baseAPI import BaseAPI
from libs.login import Login


class Shop(BaseAPI):  # 店铺模块的 业务类名--使用这个类名去获取yml里面对应接口详情
    # 2.编辑接口---id 判断需要更新
    def update(self, shop_id, image_info, in_data):
        # 如果是正向用例，这个id要更新
        if in_data['id'] == '${id}':
            in_data['id'] = shop_id
        # 图片信息
        in_data['image_path'] = image_info
        in_data['image'] = f'/file/getImgStream?fileName={image_info}'
        # 使用父类update
        return super(Shop, self).update(data=in_data)


# if __name__ == '__main__':
#     # 1.登录操作
#     login_data = {'username': 'th0198', 'password': 'xintian'}
#     token = Login().login(login_data, get_token=True)
#     # 创建店铺实例
#     shop = Shop(token)
#     # 2.店铺的查询
#     query_data = {'page': 1, 'limit': 20}
#     shop_id = shop.query(query_data)['data']['records'][0]['id']
#     print('店铺的id--->', shop_id)
#
#     # 3.图片上传接口----为了获取图片信息给编辑店铺接口
#     file_res = shop.file_upload('../data/456.png')['data']['realFileName']
#     print('文件上传信息--->', file_res)
#
#     # 4.店铺更新接口
#     update_data = {
#         "name": "星巴克新建店",
#         "address": "上海市静安区秣陵路303号",
#         "id": "${id}",
#         "Phone": "13176876632",
#         "rating": "6.0",
#         "recent_order_num": 100,
#         "category": "快餐便当/简餐",
#         "description": "满30减5，满60减8",
#         "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
#         "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
#     }
#     res2 = shop.update(shop_id, file_res, update_data)
#     print(res2)
    """
    自动化测试用例类型：
        - 正向用例/正确用例
            - 涉及到id  实时数据，需要关联更新，再运行！
        - 逆向用例/异常用例
            - 会故意写一个无效的值
    用例的数据更新理念：
        - 需要更新的时候更新，异常用例id就是不存在的，不能去更新
        - 使用if判断！----？？？
        在用例里，需要更新的数据 ${id}
        
    方法的重写：父类已经存在的方法，不能满足某一个子类的需求，子类可以重写定义这个同名方法
    

    
    """
