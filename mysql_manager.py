
import pymysql
import json


class MySQL_manager(object):

    def __init__(self, server='localhost', root='root', pw='rootroot', db='firstDB'):
        self.__server = server
        self.__root = root
        self.__pw = pw
        self.__db = db

    def mysql_version(self):
        # 连接数据库
        db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
        # 获取游标对象
        cursor = db.cursor()
        # 执行SQL命令
        cursor.execute("SELECT VERSION()")
        # 获取单条数据
        data = cursor.fetchone()
        print("Database version: %s" % data)
        # 关闭数据库连接
        db.close()

    def create_table(self):
        db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
        cursor = db.cursor()
        # 如果表存在则删除
        cursor.execute('DROP TABLE IF EXISTS tableTest')

        # 创建新表 id 自增主键
        sql = '''CREATE TABLE sdk_config (
                    id int auto_increment primary key,
                    userID text,
                    permissions int,
                    data json)'''
        cursor.execute(sql)

        sql = 'alter table sdk_config auto_increment=1'
        cursor.execute(sql)

        db.close()

    def insert_data(self, user_id='1000', data=''):
        if data == '':
            return
        db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
        cursor = db.cursor()
        # 转json数据 ensure_ascii=False, 才可以包含非ascii字符\
        json_str = json.dumps(data, ensure_ascii=False)
        # print(json_str)
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
            print('insert success')
        except:
            # 如果发生错误则回滚
            print('insert error')
            db.rollback()
        db.close()

    def fetch_data(self, user_id='1000'):
        db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
        cursor = db.cursor()
        data_arr = []
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
                print("id = %d, userID = %s, permissions = %d data = %s" % (id, userID, permissions, json.loads(data)))
        except:
            print("Error: unable to fetch data")
        db.close()
        return data_arr

    def update_data(self, id=0, data=''):
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
        except:
            db.rollback()
        db.close()

    def delete_data(self, id=0):
        if id == 0:
            return
        db = pymysql.connect(self.__server, self.__root, self.__pw, self.__db)
        cursor = db.cursor()
        # 删除
        sql = "delete from sdk_config where id = %d and permissions = 1" % id
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()


if __name__ == '__main__':
    # connect_sql()
    # create_table()
    #
    # dic = {'name': '默认配置', 'snuser': 'appjiangcimangthreathuntercn', 'applicationId': 'default',
    #        'collectURL': 'https://zqjBWuxbXzrk.yazx.com', 'snkey': '', 'version': '12',
    #        'publicKey': '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxHJS9F8OwaDDfJfEp1NfT7voRTOeWMDPPpFKvDkiB6UUmvoUCHv2LsNUYua5CREtP0m0c5UpkV9/o8cO8YcCZhqfVTUJjRMqaFU1BKSljI2ze2kc6F+IST9Y/JmodPzPe2+aOWsep3F1aMi2WZY70ldmB+3GwX4EKkZs36BHq2tWZmSVUwHSrGE0EaqEGfWWQFT3cHIHtDiuzm/3NYU9+J4KDN64mHAQxgAvjDMugUAob0atgfoB/6NByK+e1BgBtvOS4eHi/Pk2rjm2I+G6XWc1psW7BGW7BvjqDaddyi/rRVgSWfdDrgR17f2CtpPIMx10MVm8/Y0ytTXj/+upKQIDAQAB-----END PUBLIC KEY-----'}
    # insert_data('1001', dic)

    # dic = {'name': '默认配置', 'snuser': 'appjiangcimangthreathuntercn', 'applicationId': 'default',
    #        'collectURL': 'https://zqjBWuxbXzrk.yazx.com', 'snkey': '', 'version': '12',
    #        'publicKey': ''}
    # update_data(2, dic)

    # delete_data(3)
    #
    manager = MySQL_manager()
    manager.fetch_data('1001')

