
import json, mysql_manager
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
# 定义返回的数据
dataArr = [
    {
        'name': '默认配置',
        'snuser': 'appjiangcimangthreathuntercn',
        'applicationId': 'default',
        'publicKey': '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxHJS9F8OwaDDfJfEp1NfT7voRTOeWMDPPpFKvDkiB6UUmvoUCHv2LsNUYua5CREtP0m0c5UpkV9/o8cO8YcCZhqfVTUJjRMqaFU1BKSljI2ze2kc6F+IST9Y/JmodPzPe2+aOWsep3F1aMi2WZY70ldmB+3GwX4EKkZs36BHq2tWZmSVUwHSrGE0EaqEGfWWQFT3cHIHtDiuzm/3NYU9+J4KDN64mHAQxgAvjDMugUAob0atgfoB/6NByK+e1BgBtvOS4eHi/Pk2rjm2I+G6XWc1psW7BGW7BvjqDaddyi/rRVgSWfdDrgR17f2CtpPIMx10MVm8/Y0ytTXj/+upKQIDAQAB-----END PUBLIC KEY-----',
        'collectURL': 'https://zqjBWuxbXzrk.yazx.com',
        'snkey': '',
        'version': '1.0.0',
    },
    {
        'name': 'Check token',
        'snuser': 'appjiangcimangthreathuntercn',
        'applicationId': 'default',
        'publicKey': '',
        'collectURL': 'https://rcapi.threathunter.cn',
        'snkey': 'G@>r@#atxwbJt1f7-nRByQUBj@1UJ>ul',
        'version': '1.0.0'
    },
    {
        'name': '完美世界',
        'snuser': 'TomdoXQ8shq7wVdU',
        'applicationId': 'default',
        'publicKey': '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2NTQTGYVQ7EMJU+sjaY4Xp09MowG4lZpeyHLm0u14gVGFovbmXNJf35Xw+3NbsGGkr7VcTqEK8rFKSxeS6PHHDQiM66IZ4ge7d9itydaI2NrXy5X4U6KiIFh5VoTk5Uv8X/uUqLeAWTa1lHeY+8JbDKyweTUcnhDh0j/LErM1CBaUVJUF4h+JFnrJcIL+Zf+RG+VeAe9yDioleCiDDgeZ0Pe5n/6fC5mldiFhbT85wKFG7A80Gj2sbrlvzMybb1A9bttxXZOHtPqkCXse5g5td8opJfV+HtHMF2KM9wf41F8lwKU+FPo+JBVWNZ8C078NrxsDk1sRqPsLgjuJmBNxwIDAQAB-----END PUBLIC KEY-----',
        'collectURL': 'http://182.61.172.131:7006',
        'snkey': 'bpeN_ZF,oLonHM|Stu2m_dHjdPxA~7vl',
        'version': '1.0.0'
    }
]


def request_api(environ, start_response):
    # 获取请求方式
    request_method = environ['REQUEST_METHOD']
    response_dic = {}
    # 域名路径
    path_info = environ['PATH_INFO']
    print('PATH_INFO:', path_info)

    # GET请求
    if request_method == 'GET':
        # 定义响应状态、响应数据的格式
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html;charset=utf-8')]
        # 处理数据
        if path_info == '/get':
            response_dic = path_get(environ)
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
    print('params:', params)
    value = params.get('num', [''])[0]
    # 默认值
    num = 0
    # 判断是否位数字
    if value.isdigit():
        num = int(value)
    if num > 0 and num <= len(dataArr):
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
            print('request_body:', request_body)
            value = str(request_body['num'])
            # 默认值
            num = 0
            if value.isdigit():
                num = int(value)
            if num > 0 and num <= len(dataArr):
                arr = []
                for index in range(0, num):
                    arr.append(dataArr[index])
                return {'code': '200', 'data': arr}
    return {'code': '200', 'data': dataArr}


'''
'''
class server_manager(object):

    def __init__(self):
        self.mysql = mysql_manager.MySQL_manager()

    def request_api(self, environ, start_response):
        # 获取请求方式
        request_method = environ['REQUEST_METHOD']
        response_dic = {}
        # 域名路径
        path_info = environ['PATH_INFO']
        print('PATH_INFO:', path_info)

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
                print('request_body:', request_body)
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
                # print('request_body:', request_body)
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
                print('request_body:', request_body)
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
                print('request_body:', request_body)
                self.mysql.update_data(request_body['id'], request_body['data'])
                return {'code': '200', 'data': self.mysql.fetch_data(request_body['userID'])}

        return {'code': '-100', 'data': 'NULL'}


if __name__ == '__main__':
    ip = ''
    port = 8000
    http = make_server(ip, port, server_manager().request_api)
    print('serving http on port {0}...'.format(str(port)))
    http.serve_forever()
