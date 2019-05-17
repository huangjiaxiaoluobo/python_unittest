#!/usr/bin/python
# coding=utf-8
# 作者      :BuYang
# 创建时间  :2019/5/17 9:27
# 文件      :mysql_db.py
# IDE       :PyCharm

import configparser
import pymysql.cursors

# ========== 读取dbconfig.ini配置============
fp = configparser.ConfigParser()
fp.read('dbconfig.ini', encoding="utf-8")

# 读取指定节点的配置
host = fp.get("mysql_config", "host")
port = fp.get("mysql_config", "port")
user = fp.get("mysql_config", "user")
pwd = fp.get("mysql_config", "password")
db_name = fp.get("mysql_config", "db_name")
charset = fp.get("mysql_config", "charset")

mysql_config = {
    "host": host,
    "port": int(port),
    "user": user,
    "password": pwd,
    "db": str(db_name),
    "charset": charset
}


# =================数据库操作================
class OperateDb(object):

    def __init__(self):
        try:
            # 连接数据库
            # print mysql_config["db_name"]
            self.connection = pymysql.connect(**mysql_config)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        self.cursor = self.connection.cursor()

    # 关闭数据库连接
    def close_connect(self):
        self.cursor.close()
        self.connection.close()

    # 查询数据
    def query_db(self, sql, is_one=False):
        self.cursor.execute(sql)
        # 返回几条数据
        if is_one:
            result = self.cursor.fetchone()
        else:
            result = self.cursor.fetchall()
        return result


if __name__ == "__main__":
    opdb = OperateDb()
    id_list = ['10024644475498', '10024653005498']
    res_list = []

    for i in id_list:
        sql_01 = "SELECT id FROM `cargo_10` where id = {}".format(i)
        res = opdb.query_db(sql=sql_01)
        res_list.append(res)
    print(res_list)
    print(res_list[0][0][0])
    print(res_list[1][0][0])

    opdb.close_connect()
