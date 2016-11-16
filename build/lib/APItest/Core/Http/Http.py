#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'


import requests
import time
from Common.Log import Log
from Common.Data import InputData
from Common.Exception import HandleException



'''
发送http请求，返回http请求结果集
'''


class HTTP_REQUEST(object):

    def __init__(self, interfacename, casename):
        # 获取接口入参数据
        http_data = InputData.INPUTDATA().read_inputdata(interfacename, casename)
        self.inputdata = InputData.INPUTDATA().http_indata(http_data, interfacename, casename)
        self.host = self.inputdata['host']
        if self.inputdata['headers'] != None:
            self.headers = eval(self.inputdata['headers'])
        else:
            self.headers = None
        self.data = self.inputdata['data']
        self.params = self.inputdata['params']
        self.method = self.inputdata['method']
        if self.inputdata['cookie'] != None:
            self.cookie = eval(self.inputdata['cookie'])
        else:
            self.cookie = None

    def http_req(self):
        # 不同method请求发送,返回请求结果集
        try:
            if self.method.lower() == 'get':
                r = requests.Session()
                r.keep_alive = False
                self.req = r.get(url=self.host, params=self.params, headers=self.headers, data=self.data, cookies=self.cookie)
                r.close()
                self.req.close()
                return self.req
            elif self.method.lower() == 'post':
                r = requests.Session()
                r.keep_alive = False
                self.req = r.post(url=self.host, params=self.params, headers=self.headers, data=self.data, cookies=self.cookie)
                r.close()
                self.req.close()
                return self.req
            elif self.method.lower() == 'put':
                r = requests.Session()
                r.keep_alive = False
                self.req = r.put(url=self.host, params=self.params, headers=self.headers, data=self.data, cookies=self.cookie)
                r.close()
                self.req.close()
                return self.req
            elif self.method.lower() == 'patch':
                r = requests.Session()
                r.keep_alive = False
                self.req = r.patch(url=self.host, params=self.params, headers=self.headers, data=self.data,
                                 cookies=self.cookie)
                r.close()
                self.req.close()
                return self.req
            elif self.method.lower() == 'delete':
                r = requests.Session()
                r.keep_alive = False
                self.req = r.delete(url=self.host, params=self.params, headers=self.headers, data=self.data,
                                   cookies=self.cookie)
                r.close()
                self.req.close()
                return self.req
            else:
                Log.LOG(self.host).log_info('The method of Http Request is invalid!')
                return None
        except Exception, e:
            Log.LOG(self.host).log_error(e)


class HTTP_RESPONSE(object):

    def __init__(self, req):
        self.req = req

    def http_res(self):
        # 取出返回数据
        self.result = {}
        if self.req.status_code:
            self.result['req_status'] = self.req.status_code
        else:
            self.result['req_status'] = None
        if self.req.headers:
            self.result['req_headers'] = self.req.headers
        else:
            self.result['req_headers'] = None
        if self.req.content:
            self.result['req_content'] = self.req.content
        else:
            self.result['req_content'] = None
        if self.req.cookies:
            self.result['req_token'] = self.req.cookies.items()[0][1]
        else:
            self.result['req_token'] = None
        if self.req.cookies:
            self.result['req_cookie'] = self.req.cookies
        else:
            self.result['req_cookie'] = None
        return self.result

    def print_responsedata(self):
        s = '----------------response start----------------'
        s = s + '\n' + 'The data of response:' + '\n' + 'The return status:' + str(self.result['req_status'])
        s = s + '\n' + 'The return headers:' + str(self.result['req_headers'])
        s = s + '\n' + 'The return content:' + str(self.result['req_content'])
        s = s + '\n' + 'The return cookies: ' + str(self.result['req_cookie'])
        s = s + '\n' + 'The return token: ' + str(self.result['req_token'])
        s = s + '\n' + '----------------response end----------------'
        Log.LOG().log_info(s)


def http_runner(interfacename, casename):
    try:
        req = HTTP_REQUEST(interfacename, casename)
        request = req.http_req()
        # 开始response处理
        res = HTTP_RESPONSE(request)
        result = res.http_res()
        res.print_responsedata()

        return result

    except Exception,e:
        HandleException.Exception().exception('httprunner raise exception:\n'+ e)


if __name__ == '__main__':
    start = time.clock()
    res = http_runner('httpbin', 'right')
    end = time.clock()
    print 'The time of runing Http is:', end - start





