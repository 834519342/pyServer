# @Author: TJ
#
# @Time: 2020/8/12

import json
from loguru import logger
from flask import Flask, request
import mysql_manager
from mysql_manager import dataArr


app = Flask(__name__)


@app.route('/getAllConfig', methods=['POST', 'GET'])
def get_all_config():
    user_id = '1000'
    try:
        if request.method == 'POST':
            try:  # json格式
                json_data = request.get_data()
                json_dic = json.loads(json_data)
                user_id = json_dic['userID']
            except json.decoder.JSONDecodeError as e:
                logger.error(e)
                # form格式
                user_id = request.form['userID']

        elif request.method == 'GET':
            user_id = request.args.get('userID')
    except Exception as e:
        logger.exception('Exception: %s | What?' % e)
        return {'code': '-100', 'data': 'NULL'}

    return {'code': '200', 'data': mysql.fetch_data(user_id)}


@app.route('/insertConfig', methods=['POST'])
def insert_config():
    user_id = '1000'
    try:
        if request.method == 'POST':
            try:  # json格式
                json_data = request.get_data()
                json_dic = json.loads(json_data)
                user_id = json_dic['userID']
                data = json_dic['data']
            except json.decoder.JSONDecodeError as e:
                logger.error(e)
                # form格式
                user_id = request.form['userID']
                data = request.form['data']

            mysql.insert_data(user_id, data)

    except Exception as e:
        logger.exception('Exception: %s | What?' % e)
        return {'code': '-100', 'data': 'NULL'}

    return {'code': '200', 'data': mysql.fetch_data(user_id)}


@app.route('/deleteConfig', methods=['POST'])
def delete_config():
    user_id = '1000'
    try:
        if request.method == 'POST':
            try:  # json格式
                json_data = request.get_data()
                json_dic = json.loads(json_data)
                db_id = json_dic['id']
                user_id = json_dic['userID']
            except json.decoder.JSONDecodeError as e:
                logger.error(e)
                # form格式
                db_id = request.form['id']
                user_id = request.form['userID']

            mysql.delete_data(db_id)

    except Exception as e:
        logger.exception('Exception: %s | What?' % e)
        return {'code': '-100', 'data': 'NULL'}

    return {'code': '200', 'data': mysql.fetch_data(user_id)}


@app.route('/updateConfig', methods=['POST'])
def update_config():
    user_id = '1000'
    try:
        if request.method == 'POST':
            try:  # json格式
                json_data = request.get_data()
                json_dic = json.loads(json_data)
                db_id = json_dic['id']
                user_id = json_dic['userID']
                data = json_dic['data']
            except json.decoder.JSONDecodeError as e:
                logger.error(e)
                # form格式
                db_id = request.form['id']
                user_id = request.form['userID']
                data = request.form['data']

            mysql.update_data(db_id, data)

    except Exception as e:
        logger.exception('Exception: %s | What?' % e)
        return {'code': '-100', 'data': 'NULL'}

    return {'code': '200', 'data': mysql.fetch_data(user_id)}


if __name__ == '__main__':
    mysql = mysql_manager.MySQL_manager()
    # app.debug = True  # 调试模式
    app.run(port='9090')