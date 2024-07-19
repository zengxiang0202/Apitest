# -*- coding: utf-8 -*-
# @File    : mock_server
# @Author  : zengxiang0202
# @Email   : 948795152@qq.com
# @Software: PyCharm
# Date: 2024/7/19
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"message":"hello，你已进入mock服务"})

# Mock endpoint for order creation
@app.route('/api/order/create/', methods=['POST'])
def create_order():
    data = request.get_json()
    return jsonify({"order_id": "mock_order_id_123"})

# Mock endpoint for getting order result
@app.route('/api/order/get_result01/', methods=['GET'])
def get_order_result():
    order_id = request.args.get('order_id')
    if order_id == 'mock_order_id_123':
        return jsonify({"status": "success", "result": "Order completed"})
    else:
        return jsonify({}), 204

if __name__ == '__main__':
    app.run(port=9999)
