import pymysql
import json
from loguru import logger
import os


module_name = str(os.path.basename(__file__)).split('.')[0]  # 模块名
logger.add("logs/%s.log" % module_name, rotation="10:00", encoding="utf-8", retention="3 days")

# 默认数据
dataArr = [
    {
        "userID": "1000",
        "name": "默认配置",
        "snkey": "",
        "snuser": "appjiangcimangthreathuntercn",
        "version": "12",
        "publicKey": "-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxHJS9F8OwaDDfJfEp1NfT7voRTOeWMDPPpFKvDkiB6UUmvoUCHv2LsNUYua5CREtP0m0c5UpkV9/o8cO8YcCZhqfVTUJjRMqaFU1BKSljI2ze2kc6F+IST9Y/JmodPzPe2+aOWsep3F1aMi2WZY70ldmB+3GwX4EKkZs36BHq2tWZmSVUwHSrGE0EaqEGfWWQFT3cHIHtDiuzm/3NYU9+J4KDN64mHAQxgAvjDMugUAob0atgfoB/6NByK+e1BgBtvOS4eHi/Pk2rjm2I+G6XWc1psW7BGW7BvjqDaddyi/rRVgSWfdDrgR17f2CtpPIMx10MVm8/Y0ytTXj/+upKQIDAQAB-----END PUBLIC KEY-----",
        "collectURL": "https://nmpbosr72matlv-device-fingerprint.yazx.com",
        "applicationId": "default"
    },
    {
        "userID": "1000",
        "name": "Check token",
        "snkey": "G@>r@#atxwbJt1f7-nRByQUBj@1UJ>ul",
        "snuser": "appjiangcimangthreathuntercn",
        "version": "12",
        "publicKey": "-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxHJS9F8OwaDDfJfEp1NfT7voRTOeWMDPPpFKvDkiB6UUmvoUCHv2LsNUYua5CREtP0m0c5UpkV9/o8cO8YcCZhqfVTUJjRMqaFU1BKSljI2ze2kc6F+IST9Y/JmodPzPe2+aOWsep3F1aMi2WZY70ldmB+3GwX4EKkZs36BHq2tWZmSVUwHSrGE0EaqEGfWWQFT3cHIHtDiuzm/3NYU9+J4KDN64mHAQxgAvjDMugUAob0atgfoB/6NByK+e1BgBtvOS4eHi/Pk2rjm2I+G6XWc1psW7BGW7BvjqDaddyi/rRVgSWfdDrgR17f2CtpPIMx10MVm8/Y0ytTXj/+upKQIDAQAB-----END PUBLIC KEY-----",
        "collectURL": "https://rcapi.yazx.com",
        "applicationId": "default"
    },
    {
        "userID": "1000",
        "name": "完美世界",
        "snkey": "bpeN_ZF,oLonHM|Stu2m_dHjdPxA~7vl",
        "snuser": "TomdoXQ8shq7wVdU",
        "version": "12",
        "publicKey": "-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2NTQTGYVQ7EMJU+sjaY4Xp09MowG4lZpeyHLm0u14gVGFovbmXNJf35Xw+3NbsGGkr7VcTqEK8rFKSxeS6PHHDQiM66IZ4ge7d9itydaI2NrXy5X4U6KiIFh5VoTk5Uv8X/uUqLeAWTa1lHeY+8JbDKyweTUcnhDh0j/LErM1CBaUVJUF4h+JFnrJcIL+Zf+RG+VeAe9yDioleCiDDgeZ0Pe5n/6fC5mldiFhbT85wKFG7A80Gj2sbrlvzMybb1A9bttxXZOHtPqkCXse5g5td8opJfV+HtHMF2KM9wf41F8lwKU+FPo+JBVWNZ8C078NrxsDk1sRqPsLgjuJmBNxwIDAQAB-----END PUBLIC KEY-----",
        "collectURL": "http://182.61.172.131:7006",
        "applicationId": "default"
    },
    {
        "userID": "1001",
        "name": "aaa",
        "snkey": "G@>r@#atxwbJt1f7-nRByQUBj@1UJ>ul",
        "snuser": "appjiangcimangthreathuntercn",
        "version": "13",
        "publicKey": "-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxHJS9F8OwaDDfJfEp1NfT7voRTOeWMDPPpFKvDkiB6UUmvoUCHv2LsNUYua5CREtP0m0c5UpkV9/o8cO8YcCZhqfVTUJjRMqaFU1BKSljI2ze2kc6F+IST9Y/JmodPzPe2+aOWsep3F1aMi2WZY70ldmB+3GwX4EKkZs36BHq2tWZmSVUwHSrGE0EaqEGfWWQFT3cHIHtDiuzm/3NYU9+J4KDN64mHAQxgAvjDMugUAob0atgfoB/6NByK+e1BgBtvOS4eHi/Pk2rjm2I+G6XWc1psW7BGW7BvjqDaddyi/rRVgSWfdDrgR17f2CtpPIMx10MVm8/Y0ytTXj/+upKQIDAQAB-----END PUBLIC KEY-----",
        "collectURL": "https://qwtzfuv4h-private-device-fingerprint.yazx.com",
        "applicationId": "default"
    },
    {
        "userID": "1001",
        "name": "Ceshi",
        "snkey": "G@>r@#atxwbJt1f7-nRByQUBj@1UJ>ul",
        "snuser": "appjiangcimangthreathuntercn",
        "version": "13",
        "publicKey": "-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxHJS9F8OwaDDfJfEp1NfT7voRTOeWMDPPpFKvDkiB6UUmvoUCHv2LsNUYua5CREtP0m0c5UpkV9/o8cO8YcCZhqfVTUJjRMqaFU1BKSljI2ze2kc6F+IST9Y/JmodPzPe2+aOWsep3F1aMi2WZY70ldmB+3GwX4EKkZs36BHq2tWZmSVUwHSrGE0EaqEGfWWQFT3cHIHtDiuzm/3NYU9+J4KDN64mHAQxgAvjDMugUAob0atgfoB/6NByK+e1BgBtvOS4eHi/Pk2rjm2I+G6XWc1psW7BGW7BvjqDaddyi/rRVgSWfdDrgR17f2CtpPIMx10MVm8/Y0ytTXj/+upKQIDAQAB-----END PUBLIC KEY-----",
        "collectURL": "https://nmpbosr72matlv-device-fingerprint.yazx.com",
        "applicationId": "default"
    },
]


class MySQL_manager(object):

    def __init__(self, server='localhost', root='root', pw='rootroot', db='ios_sdk_db'):
        self.__server = server
        self.__root = root
        self.__pw = pw
        self.__db = db

    # 测试是否连通
    def mysql_version(self):
        try:
            # 连接数据库
            db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
            # 获取游标对象
            cursor = db.cursor()
            # 执行SQL命令
            cursor.execute("SELECT VERSION()")
            # 获取单条数据
            data = cursor.fetchone()
            logger.info("Database version: %s" % data)
            # 关闭数据库连接
            cursor.close()
            db.close()
        except Exception as e:
            logger.exception('Exception: %s | What?' % e)

    # 重置表
    def reset_table(self):
        try:
            db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
            cursor = db.cursor()
            # 如果表存在则删除
            cursor.execute('DROP TABLE IF EXISTS sdk_config')

            # 创建新表 id 自增主键
            sql = '''CREATE TABLE sdk_config (
                        id int auto_increment primary key,
                        userID text,
                        permissions int,
                        data text)'''
            cursor.execute(sql)

            sql = 'alter table sdk_config auto_increment=1'
            cursor.execute(sql)

            cursor.close()
            db.close()
        except Exception as e:
            logger.exception('Exception: %s | What?' % e)

    def insert_data(self, user_id='1000', data=None):
        try:
            if not data:
                return
            db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
            cursor = db.cursor()
            # 转json数据 ensure_ascii=False, 才可以包含非ascii字符\
            json_str = json.dumps(data, ensure_ascii=False)
            logger.info(json_str)
            # 编辑权限
            permissions = 1
            if user_id == '1000':
                permissions = 0
            # 插入数据
            sql = "insert into sdk_config(userID, data, permissions) VALUES ('%s', '%s', %d)" %\
                  (user_id, json_str, permissions)
            try:
                cursor.execute(sql)
                # 提交到数据库
                db.commit()
                logger.info('insert success')
            except Exception as e:
                # 如果发生错误则回滚
                db.rollback()
                logger.exception('Exception: %s | What?' % e)

            cursor.close()
            db.close()
        except Exception as e:
            logger.exception('Exception: %s | What?' % e)

    def fetch_data(self, user_id='1000'):
        try:
            db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
            cursor = db.cursor()
            data_arr = list()
            # 查询
            sql = "select * from sdk_config where userID = '1000' or userID = '%s'" % user_id
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    id = row[0]
                    userID = row[1]
                    permissions = row[2]
                    data = row[3]
                    dic = {'id': id, 'userID': userID, 'permissions': permissions, 'data': json.loads(data)}
                    data_arr.append(dic)
                    logger.info("id = %d, userID = %s, permissions = %d data = %s" % (id, userID, permissions, json.loads(data)))
            except Exception as e:
                logger.exception('Exception: %s | What?' % e)

            cursor.close()
            db.close()
            return data_arr
        except Exception as e:
            logger.exception('Exception: %s | What?' % e)

    def update_data(self, id=0, data=''):
        try:
            if id == 0 or data == '':
                return
            db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
            cursor = db.cursor()
            # 更新
            json_str = json.dumps(data, ensure_ascii=False)
            sql = "update sdk_config set data = '%s' where id = %d and permissions = 1" % (json_str, id)
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                # 如果发生错误则回滚
                db.rollback()
                logger.exception('Exception: %s | What?' % e)

            cursor.close()
            db.close()
        except Exception as e:
            logger.exception('Exception: %s | What?' % e)

    def delete_data(self, id=0):
        try:
            if id == 0:
                return
            db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
            cursor = db.cursor()
            # 删除
            sql = "delete from sdk_config where id = %d and permissions = 1" % id
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                # 如果发生错误则回滚
                db.rollback()
                logger.exception('Exception: %s | What?' % e)

            cursor.close()
            db.close()
        except Exception as e:
            logger.exception('Exception: %s | What?' % e)


if __name__ == '__main__':
    manager = MySQL_manager()
    manager.mysql_version()
    manager.reset_table()

    for data_dic in dataArr:
        manager.insert_data(data_dic["userID"], data_dic)

    manager.fetch_data('1001')
