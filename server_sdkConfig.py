import json
import mysql_manager
from mysql_manager import dataArr
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from loguru import logger
import os


module_name = str(os.path.basename(__file__)).split('.')[0]  # 模块名
logger.add("logs/%s.log" % module_name, rotation="10:00", encoding="utf-8", retention="3 days")


def request_api(environ, start_response):
    # 获取请求方式
    request_method = environ['REQUEST_METHOD']
    response_dic = {}
    # 域名路径
    path_info = environ['PATH_INFO']
    logger.info('PATH_INFO: %s' % path_info)

    # GET请求
    if request_method == "GET":
        # 定义响应状态、响应数据的格式
        status = "200 OK"
        response_headers = [('Content-Type', 'text/html;charset=utf-8')]
        # 处理数据
        if path_info == "/get":
            response_dic = path_get(environ)
        else:
            status = "404 pathError"
            response_dic = {'error': '404'}
        start_response(status, response_headers)

    # POST请求
    if request_method == 'POST':
        # 定义响应状态、响应数据的格式
        status = '200 OK'
        response_headers = [('Content-Type', 'application/json')]
        # 处理数据
        if path_info == '/post':
            response_dic = path_post(environ)
        else:
            status = '404 pathError'
        start_response(status, response_headers)

    return [json.dumps(response_dic).encode('utf-8')]


# /get 路径处理
def path_get(environ):
    # 获取网址附带参数 域名/?num=[1-3]
    params = parse_qs(environ['QUERY_STRING'])
    logger.info('params: %s' % params)
    value = params.get('num', [''])[0]
    # 默认值
    num = 0
    # 判断是否位数字
    if value.isdigit():
        num = int(value)
    if 0 < num <= len(dataArr):
        arr = []
        for index in range(0, num):
            arr.append(dataArr[index])
        return {'code': '200', 'data': arr}
    return {'code': '200', 'data': dataArr}


# /post 路径处理
def path_post(environ):
    # 获取请求附带的body参数 {num: [1-3]}
    content_length = environ['CONTENT_LENGTH']
    # 判断是否为数字
    if content_length.isdigit():
        body_length = int(content_length)
        if body_length > 4:
            # 获取请求参数
            request_body = environ['wsgi.input'].read(body_length)
            request_body = json.loads(request_body)
            logger.info('request_body: %s' % request_body)
            value = str(request_body['num'])
            # 默认值
            num = 0
            if value.isdigit():
                num = int(value)
            if 0 < num <= len(dataArr):
                arr = []
                for index in range(0, num):
                    arr.append(dataArr[index])
                return {'code': '200', 'data': arr}
    return {'code': '200', 'data': dataArr}


class server_manager(object):

    def __init__(self):
        self.mysql = mysql_manager.MySQL_manager()

    def request_api(self, environ, start_response):
        # 获取请求方式
        request_method = environ['REQUEST_METHOD']
        response_dic = {}
        # 域名路径
        path_info = environ['PATH_INFO']
        logger.info('PATH_INFO: %s' % path_info)

        # GET请求
        if request_method == 'GET':
            # 定义响应状态、响应数据的格式
            status = '200 OK'
            response_headers = [('Content-Type', 'text/html;charset=utf-8')]
            # 处理数据
            if path_info == '':
                pass
            else:
                status = '404 pathError'
                response_dic = {'error': '404'}
            start_response(status, response_headers)

        # POST请求
        if request_method == 'POST':
            # 定义响应状态、响应数据的格式
            status = '200 OK'
            response_headers = [('Content-Type', 'application/json')]
            # 处理数据
            if path_info == '/getAllConfig':
                response_dic = self.get_all_config(environ)
            elif path_info == '/insertConfig':
                response_dic = self.insert_config(environ)
            elif path_info == '/deleteConfig':
                response_dic = self.delete_config(environ)
            elif path_info == '/updateConfig':
                response_dic = self.update_config(environ)
            else:
                status = '404 pathError'
            start_response(status, response_headers)

        return [json.dumps(response_dic).encode('utf-8')]

    # --------------------------  MySql数据库处理 -------------------------
    def get_all_config(self, environ):
        # 获取请求附带的body参数 {num: [1-3]}
        content_length = environ['CONTENT_LENGTH']
        # 判断是否为数字
        if content_length.isdigit():
            body_length = int(content_length)
            if body_length > 4:
                # 获取请求参数
                request_body = environ['wsgi.input'].read(body_length)
                request_body = json.loads(request_body)
                logger.info('request_body: %s' % request_body)
                return {'code': '200', 'data': self.mysql.fetch_data(request_body['userID'])}

        return {'code': '-100', 'data': 'NULL'}

    def insert_config(self, environ):
        # 获取请求附带的body参数 {num: [1-3]}
        content_length = environ['CONTENT_LENGTH']
        # 判断是否为数字
        if content_length.isdigit():
            body_length = int(content_length)
            if body_length > 4:
                # 获取请求参数
                request_body = environ['wsgi.input'].read(body_length)
                request_body = json.loads(request_body)
                logger.info('request_body: %s' % request_body)
                self.mysql.insert_data(request_body['userID'], request_body['data'])
                return {'code': '200', 'data': self.mysql.fetch_data(request_body['userID'])}

        return {'code': '-100', 'data': 'NULL'}

    def delete_config(self, environ):
        # 获取请求附带的body参数 {num: [1-3]}
        content_length = environ['CONTENT_LENGTH']
        # 判断是否为数字
        if content_length.isdigit():
            body_length = int(content_length)
            if body_length > 4:
                # 获取请求参数
                request_body = environ['wsgi.input'].read(body_length)
                request_body = json.loads(request_body)
                logger.info('request_body: %s' % request_body)
                self.mysql.delete_data(request_body['id'])
                return {'code': '200', 'data': self.mysql.fetch_data(request_body['userID'])}

        return {'code': '-100', 'data': 'NULL'}

    def update_config(self, environ):
        # 获取请求附带的body参数 {num: [1-3]}
        content_length = environ['CONTENT_LENGTH']
        # 判断是否为数字
        if content_length.isdigit():
            body_length = int(content_length)
            if body_length > 4:
                # 获取请求参数
                request_body = environ['wsgi.input'].read(body_length)
                request_body = json.loads(request_body)
                logger.info('request_body: %s' % request_body)
                self.mysql.update_data(request_body['id'], request_body['data'])
                return {'code': '200', 'data': self.mysql.fetch_data(request_body['userID'])}

        return {'code': '-100', 'data': 'NULL'}


if __name__ == '__main__':
    ip = ''
    port = 9090
    http = make_server(ip, port, server_manager().request_api)
    logger.info('serving http on port %s...' % port)
    http.serve_forever()
