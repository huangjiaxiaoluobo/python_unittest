#!/usr/bin/python
# coding=utf-8
# 作者      :BuYang
# 创建时间  :2019/5/16 10:46
# 文件      :queryPaymentTypeByMedia_test.py
# IDE       :PyCharm

import unittest
import json
from test_unittest.api.queryPaymentTypeByMedia import QueryPaymentTypeByMedia
from test_unittest.db_fixture.mysql_db import OperateDb


class QueryPaymentTypeByMediaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.queryPaymentTypeByMedia = QueryPaymentTypeByMedia()
        # 初始media测试数据
        cls.media = ["testwlj_prepaid", "testwlj_postpaid"]
        # 预期的result_code数据
        cls.result_code_expect = ['0', '0']
        print("开始测试")
        print()

    def test_queryPaymentTypeByMedia_001(self):
        """
        media枚举测试：media= ["testwlj_prepaid", "testwlj_postpaid"]
        """
        # 定义一个空数组，用于存放响应中的payment_type和result_code
        payment_type_list = []
        result_code_list = []
        payment_mode_cd_list = []
        # 计数作用
        n = 0

        for i in self.media:
            data = {
                "contractRoot": {"tcpCont": {"appKey": "CPC-Service", "dstSysId": "CPCCenter ",
                                             "transactionId": "1001000101201602021234567890",
                                             "reqTime": "20170210145959001"},
                                 "svcCont": {"requestObject": {"media": i}}}
            }

            # 接口调用，这里的response是一个str类型的数据,并将str转成dict
            response = self.queryPaymentTypeByMedia.queryPaymentTypeByMedia(data)
            resp = json.loads(response)

            # 获取paymentType和result_code
            payment_type = resp['contractRoot']['svcCont']['resultObject']['paymentType'][n]
            result_code = resp['contractRoot']['svcCont']['resultCode']

            # 将接口响应中的payment_type和result_code添加到列表中
            payment_type_list.append(payment_type)
            result_code_list.append(result_code)

            # 数据库校验
            operate_db = OperateDb()  # 初始化数据库连接
            sql = "select ppm.PAYMENT_MODE_CD " \
                  "from product p,product_payment_mode ppm " \
                  "where STATUS_CD='1000' and p.PROD_ID=ppm.PRODUCT_ID and p.prod_name= {}" \
                .format(i)
            payment_type_expect = operate_db.query_db(sql)
            payment_mode_cd_list.append(payment_type_expect)  # 将数据库中的payment添加到列表中

            # 关闭数据库连接
            operate_db.close_connect()

            # 校验数据库中的payment_mode_cd_list和接口返回的payment_type_list是否一致
            self.assertEqual(payment_mode_cd_list[n][0][0], payment_type_list[n], msg=None)
            print("payment_mode_cd_list[{}]是:{},payment_type_list[{}]是{}"
                  .format(n, payment_mode_cd_list[n][0][0], n, payment_type_list[n]))
            self.assertEqual(self.result_code_expect[n], result_code_list[n], msg=None)
            print("result_code_expect[{}]是:{},result_code_list[{}]是{}"
                  .format(n, self.result_code_expect[n], n, result_code_list[n]))

            n += 1

    @classmethod
    def tearDownClass(cls):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()
