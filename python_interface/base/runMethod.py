# -*- coding: utf-8 -*-
# Time    : 2019-05-10 00:38
# Author  : BuYang
# File    : runMethod.py

import requests
import json


class RunMethod:

    def post_main(self, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data, header=None):
        if header is not None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

