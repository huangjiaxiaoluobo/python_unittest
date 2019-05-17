# -*- coding: utf-8 -*-
# Time    : 2019-05-09 23:53
# Author  : BuYang
# File    : data_config.py


class GlobalVar:
    # 定义用例模板的列名
    ID = '0'
    case_name = '1'
    URL = '2'
    request_way = "3"
    header = '4'
    data_ld_depend = '5'
    data_depend = '6'
    data_field_depend = '7'
    request_body = '8'
    expect = '9'
    result = '10'
    is_run = '11'


def get_ID():
    return GlobalVar.ID


def get_case_name():
    return GlobalVar.case_name


def get_URL():
    return GlobalVar.URL


def get_request_way():
    return GlobalVar.request_way


def get_is_header():
    return GlobalVar.header


def get_data_id_depend():
    return GlobalVar.data_ld_depend


def get_data_depend():
    return GlobalVar.data_depend


def get_data_field_depend():
    return GlobalVar.data_field_depend


def get_request_body():
    return GlobalVar.request_body


def get_expect():
    return GlobalVar.expect


def get_result():
    return GlobalVar.result


def get_is_run():
    return GlobalVar.is_run


def get_header_value():
    header = {
        "username": "buyang",
        "password": "123456"
    }
