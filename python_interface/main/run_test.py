# -*- coding: utf-8 -*-
# Time    : 2019-05-13 19:52
# Author  : BuYang
# File    : run_test.py

from python_interface.base.runMethod import RunMethod
from python_interface.data.get_data import GetData
from python_interface.util.common_util import CommonUtil


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil

    # 程序执行入口
    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            # 取出Excel中的数据
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            expect = self.data.get_expect_result(i)
            header = self.data.get_is_header(i)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
                if self.com_util().is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                else:
                    self.data.write_result(i, 'error')
                print("响应数据为：{}".format(res))
                print()


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
