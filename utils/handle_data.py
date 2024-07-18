#-*- coding: utf-8 -*-
#@File    : handle_data.py
#@Time    : 2022/8/3 22:21
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2022/8/3 
import hashlib
# 区别： “”  “ ”  None
def get_md5_data(pwd:str,salt=''):
    """
    :param pwd: 加密的明文
    :param salt: 盐值
    :return: 返回的加密后的密文
    """
    #1.创建md5实例
    md5 = hashlib.md5()
    #2.加密函数操作
    pwd = pwd+salt
    md5.update(pwd.encode('utf-8'))
    #3.返回加密后的结果
    return md5.hexdigest()#16进制数据  0123456789ABCDEF

"""
外卖项目--RSA加密接口
url = 'http://121.41.14.39:8082/account/loginRsa'
参数：
    username  账号
    password: RSA加密的结果
        1- xintian通过md5加密成密文--a
        2- 使用RSA的公钥加密(a)
    sign 签名
        md5(username+password密文)
实现：
    - 1.完成md5加密算法
    - 2.rsa加密算法
"""
#pip install  pycryptodome -i https://pypi.douban.com/sample/
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64
"""
rsa加密流程：
    前提条件：有公钥  字符串/xxx.pem
    1.输入需要加密的明文 pwd
    2.把明文密码进程编码处理  'abc' str ---转化---bytes b'abc'
    3.调用rsa库的加密函数(b‘xxx’)
    4.还得使用base64编码处理加密后的数据
    5.解码，bytes---转成---str
"""
class RsaEndecrype:
    #需要公钥文件
    def __init__(self,file_path='./public.pem'):
        self.file_path=file_path
    #加密方法
    def encrypt(self,crypt_data):
        #1.打开公钥文件，并且使用2进制打开
        with open(self.file_path,'rb') as fo:
            #2.获取g公钥的值
            key_content = fo.read()
            print(key_content)
            #3.需要对加密的明文进行转化---bytes
            crypt_data = crypt_data.encode('utf-8')
            #4.需要一个公钥对象
            public_key_object = RSA.importKey(key_content)
            #5.生成一个加密对象
            cipher_object = PKCS1_cipher.new(public_key_object)
            #6.调用加密算法---获取的是一个bytes
            res_bytes = cipher_object.encrypt(crypt_data)
            print('加密后的数据>>>',res_bytes)
            #再进过base64编码，再转化成的str
            #decode解码  把字节码--变成-字符串
            return base64.b64encode(res_bytes).decode()





if __name__ == '__main__':
    # res = get_md5_data('1232544441')
    # print(res)
    res = RsaEndecrype().encrypt('123456')
    print(res)