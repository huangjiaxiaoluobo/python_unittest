# -*- coding: utf-8 -*-
# Time    : 2019-05-14 23:05
# Author  : BuYang
# File    : common_util.py


class CommonUtil:
    """
    判断一个字符串是否在另一个字符串中
    """

    def is_contain(self, str_one, str_two):

        # if isinstance(str_one, str):
        #     str_one = str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
