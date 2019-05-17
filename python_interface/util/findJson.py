# -*- coding: utf-8 -*-
# Time    : 2019-05-15 20:14
# Author  : BuYang
# File    : findJson.py

import os


class FindJson:
    def __init__(self, dirname):
        self.dirname = dirname

    def all_path(self):
        # 所有的文件
        result = []

        """
        maindir:当前主目录
        subdir:当前主目录下的所有目录
        file_name_list:当前主目录下的所有文件
        """
        for maindir, subdir, file_name_list in os.walk(self.dirname):

            for filename in file_name_list:
                # 合并成一个完整路径
                apath = os.path.join(maindir, filename)
                # 获取文件后缀 [0]获取的是除了文件名以外的内容
                ext = os.path.splitext(apath)[1]
                # 设置过滤后的文件类型
                filter = ['.json']
                if ext in filter:
                    result.append(apath)

        return result


if __name__ == '__main__':
    all_path = FindJson("../dataconfig")
    for i in all_path.all_path():
        i = "\'{}\'".format(i)
        print(i)
