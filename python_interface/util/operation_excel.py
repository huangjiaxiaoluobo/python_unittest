# -*- coding: utf-8 -*-
# Time    : 2019-05-07 21:58
# Author  : BuYang
# File    : operation_excel.py.py

import xlrd
from xlutils.copy import copy

file_path = '../dataconfig/测试数据.xls'


class OperationExcel:

    # 定义一个构造函数
    def __init__(self, sheet_id=None, path=None):
        if path:
            self.sheet_id = sheet_id
            self.path = path
        else:
            self.path = file_path
            self.sheet_id = 0
        self.data = self.get_excel_sheet()

    # 打开Excel文件，并获取指定sheet页数据
    def get_excel_sheet(self):
        data = xlrd.open_workbook(self.path)
        sheet = data.sheets()[self.sheet_id]
        return sheet

    # 获取Excel的总行数
    def get_excel_lines(self):
        sheet = self.data
        lines = sheet.nrows
        return lines

    # 获取Excel的单元格数据
    def get_excel_cell_data(self, row, col):
        sheet = self.data
        row = int(row)
        col = int(col)
        cell_value = sheet.cell_value(row, col)
        return cell_value

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.path)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.path)

# if __name__ == '__main__':
#     op = OperationExcel()
#
#     print(op.get_excel_sheet())
#     print(op.get_excel_cell_data(1, 8))
