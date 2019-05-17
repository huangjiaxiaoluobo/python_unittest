#!/usr/bin/python
# coding=utf-8
# 作者      :BuYang
# 创建时间  :2019/5/16 10:55
# 文件      :run_method.py
# IDE       :PyCharm
import requests


class RunMethod(object):

    def post_method(self, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()
