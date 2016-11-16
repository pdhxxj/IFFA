#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import Core.Hessian as hessian
import Core.Http as http
import Core.Https as https
import time
from Common import Log


class DOBBOU(object):

    # 入参为协议类型http、https、hessian;若基于hessian
    def __init__(self, method, interfacename, apiname=''):
        self.method = method
        self.interfacename = interfacename
        self.apiname = apiname

    def hessian_runner(self):
        Log.LOG('DOBBOU').log_info('The Dobbou method:\n')
        result = hessian.hessian_runner(self.interfacename, self.apiname)
        return result

    def https_runner(self):
        Log.LOG('DOBBOU').log_info('The Dobbou method:\n')
        result = https.https_runner(self.interfacename)
        return result

    def http_runner(self):
        Log.LOG('DOBBOU').log_info('The Dobbou method:\n')
        result = http.http_runner(self.interfacename)
        return result

    def dobbou_runner(self):
        if self.method.lower() == 'http':
            res =self.http_runner()
            return res
        elif self.method.lower() == 'https':
            res = self.https_runner()
            return res
        elif self.method.lower() == 'hessian':
            res = self.hessian_runner()
            return res
        else:
            Log.LOG('DOBBOU').log_info('The protocol of Dobbou interface is invalid！')


def dobbou_runner(method, interfacename, apiname=''):
    result = DOBBOU(method,interfacename, apiname).dobbou_runner()
    return result

if __name__ == '__main__':
    start = time.clock()
    res = dobbou_runner('http', 'httpbin')
    end = time.clock()
    print 'The time of runing Http is:', end - start