#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

from Utils.File import File
import os
import Yaml
import json
from Common.Log import Log
from Common.Exception import HandleException
from Utils.Code import TransCode
from Utils.DB import  HandleDB


class INPUTDATA(object):

    def __init__(self):
        pass

    def read_bfdata(self, filename):
        r = File.FILE().read_bfile(filename)
        return r

    def print_inputdata(self, inputdata, http_data, interfacename, casename):
        # 打印入参数据
        s = '\n' + '----------------http request start----------------' + '\n' + 'The request host:' + str(inputdata['host'])
        s = s + '\n' + 'The request headers:' + str(inputdata['headers'])
        if http_data['data'] != None:
            s = s + '\n' + 'The request body:' + str(inputdata['data'])
        s = s + '\n' + 'The request params:' + str(inputdata['params'])
        s = s + '\n' + 'The request method:' + str(inputdata['method'])
        s = s + '\n' + 'The request cookie:' + str(inputdata['cookie'])
        s = s + '\n' + '----------------request end----------------'
        Log.LOG(interfacename + '->' + casename + '-->' + inputdata['host']).log_info(s)

    def get_configdata(self, interfacename):
        try:
            '''
            path = os.path.dirname(os.getcwd())
            parpath = os.path.dirname(path)
            yamlname = parpath + '/Config/interface/' + '%s/%s.yaml' % (interfacename, interfacename)
            config_data = Yaml.YAML().read_yaml(yamlname)'''
            config_data = HandleDB.HandleDB().db_readconfig(interfacename)
            return config_data
        except Exception, e:
            HandleException.Exception().exception('get_configdata raise exception:\n'+ e)

    def read_inputdata(self, interfacename, casename):
        try:
            path = os.path.dirname(os.getcwd())
            parpath = os.path.dirname(path)
            # 获取接口配置数据
            config_data = self.get_configdata(interfacename)
            case_data = config_data
            # 从case中取参数
            '''filename = parpath + '/TestCase/Function/' + '%s/%s.txt' % (interfacename, casename)
            with open(filename, 'r')as f:
                para_data = f.read()
                # 对case里取出的string流处理
                para_data = TransCode.TransCode().transcode(para_data)'''
            para_data = HandleDB.HandleDB().db_readcaseinfo(casename)
            Log.LOG(interfacename + '--->' + casename).log_result('para_data: %s\n'%para_data)
            case_data['params'] = para_data
            return case_data
        except Exception,e:
            HandleException.Exception().exception('read_inputdata raise exception:\n'+ e)

    def http_indata(self, http_data, interfacename, casename):
        try:
            path = os.path.dirname(os.getcwd())
            parpath = os.path.dirname(path)
            host = http_data['host']
            http_data['data'] = eval(http_data['data'])
            if http_data['data'] != None:
                data = json.dumps(http_data['data']['value'], ensure_ascii=False)
            else:
                data = None
            headers = http_data['headers']
            params = http_data['params']
            method = http_data['method']
            cookie = http_data['cookie']
            inputdata = {'host': host,
                    'data': data,
                    'headers': headers,
                    'params': params,
                    'method': method,
                    'cookie': cookie
                    }
            self.print_inputdata(inputdata, http_data, interfacename, casename)
            return inputdata
        except Exception,e:
            HandleException.Exception().exception('http_indata raise exception:\n' + e)

    def hessian_indata(self, interfacename, casename):
        try:
            config = HandleDB.HandleDB().db_readconfig(interfacename)
            jarname = config['jarname']
            classname = config['classname']
            funcname = config['funcname']
            host = config['host']
            # 'http://10.102.36.151:8080/hessian/orderService' # 'http://example.com/hession4.0server/remote/helloSpring'
            params = HandleDB.HandleDB().db_readcaseinfo(casename)

            inputdata = {'host': host,
                        'params': params,
                         'jarname': jarname,
                         'classname': classname,
                         'funcname': funcname
                        }
            return inputdata
        except Exception,e:
            HandleException.Exception().exception('hessian_indata raise exception:\n' + e)

    def https_indata(self, https_data, interfacename, casename):
        try:
            path = os.path.dirname(os.getcwd())
            parpath = os.path.dirname(path)
            host = https_data['host']
            if https_data['data'] != None:
                data = json.dumps(https_data['data']['value'], ensure_ascii=False)
            else:
                data = None
            headers = https_data['headers']
            params = https_data['params']
            method = https_data['method']
            cookie = https_data['cookie']

            inputdata = {'host': host,
                        'data': data,
                        'headers': headers,
                        'params': params,
                        'method': method,
                        'cookie': cookie
                        }

            self.print_inputdata(inputdata, https_data, interfacename, casename)
            return inputdata
        except Exception,e:
            HandleException.Exception().exception('https_indata raise exception:\n' + e)


if __name__ == '__main__':
    http_data = INPUTDATA().read_inputdata('httpbin', '1')
    inputdata = INPUTDATA().http_indata(http_data)
    print inputdata