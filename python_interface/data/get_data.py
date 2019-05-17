# -*- coding: utf-8 -*-
# Time    : 2019-05-10 00:05
# Author  : BuYang
# File    : get_data.py
from python_interface.data import data_config
from python_interface.util.operation_excel import OperationExcel
from python_interface.util.operation_json import OperationJson
from python_interface.util.findJson import FindJson


class GetData:

    def __init__(self):
        # 添加需要执行的测试用例文件
        sheet_id = 0
        excel_file = ['../dataconfig/测试数据.xls']
        for i in excel_file:
            self.opera_excel = OperationExcel(sheet_id, i)
        # 需要遍历json文件的路径
        find_json_path = '../dataconfig'
        self.json = FindJson(find_json_path)

    # 去获取excel的行数，对应的是case的条数
    def get_case_lines(self):
        return self.opera_excel.get_excel_lines()

    # 判断测试用例是否需要执行
    def get_is_run(self, row):
        col = data_config.get_is_run()
        run_model = self.opera_excel.get_excel_cell_data(row, col)

        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 判断是否携带header
    def get_is_header(self, row):
        col = data_config.get_is_header()
        header = self.opera_excel.get_excel_cell_data(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = data_config.get_request_way()
        request_method = self.opera_excel.get_excel_cell_data(row, col)
        return request_method

    # 获取URL
    def get_request_url(self, row):
        col = data_config.get_URL()
        request_url = self.opera_excel.get_excel_cell_data(row, col)
        return request_url

    # 获取请求数据
    def get_request_data(self, row):
        col = data_config.get_request_body()
        request_data = self.opera_excel.get_excel_cell_data(row, col)
        # 请求数据有可能是空值
        if request_data == '':
            return None
        return request_data

    # 通过关键字拿到request_data对应的json数据
    def get_data_for_json(self, row):

        json_file = self.json.all_path()
        for i in json_file:
            opera_json = OperationJson(i)
            json_data = opera_json.get_data(self.get_request_data(row))
            return json_data

    # 获取预期结果
    def get_expect_result(self, row):
        col = data_config.get_expect()
        expect_result = self.opera_excel.get_excel_cell_data(row, col)
        if expect_result == '':
            return None
        return expect_result

    # 将执行结果写入Excel
    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)
        case_id = self.opera_excel.get_excel_cell_data(row, 0)
        print("case_id:{} 的执行结果为:{}".format(case_id, value))
