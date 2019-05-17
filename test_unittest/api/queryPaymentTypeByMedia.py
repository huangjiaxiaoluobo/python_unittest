#!/usr/bin/python
# coding=utf-8
# 作者      :BuYang
# 创建时间  :2019/5/16 11:42
# 文件      :queryPaymentTypeByMedia.py
# IDE       :PyCharm

from test_unittest.util.run_method import RunMethod
import json


class QueryPaymentTypeByMedia(object):

    def queryPaymentTypeByMedia(self, data):
        url = "http://172.16.23.233/market-service/callTrueCPCService/queryPaymentTypeByMedia"
        header = {
            "Content-Type": "application/json"
        }

        res = RunMethod().post_method(url, json.dumps(data), header)
        # res是dict类型，转成str类型
        return json.dumps(res)
