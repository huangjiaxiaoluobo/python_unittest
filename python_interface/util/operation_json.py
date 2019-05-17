# -*- coding: utf-8 -*-
# Time    : 2019-05-09 23:27
# Author  : BuYang
# File    : operation_json.py

import json


class OperationJson:

    # 定义一个构造函数
    def __init__(self, path):
        self.path = path
        self.data = self.read_data()

    # 读取json数据
    def read_data(self):
        with open(self.path) as fp:
            data = json.load(fp)
            return data

    # 根据指定的key值，获取json文件中对应的数据
    def get_data(self, key):
        data = self.read_data()
        json_value = data[key]
        return json_value


if __name__ == '__main__':
    file = ['../dataconfig/user.json','../dataconfig/test.json']
    for i in file:
        op = OperationJson(i)
        print(op.get_data('user'))
        print(i)
