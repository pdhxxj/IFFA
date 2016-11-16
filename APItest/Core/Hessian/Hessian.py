#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

from Common.Data import InputData
from pyhessian.client import HessianProxy
from Utils.Jar import HandleJar
from Common.Exception import HandleException
from Utils.DB import HandleDB
import time
from Common.Log import Log


class HESSIAN_REQ(object):

    def __init__(self, interfacename, casename):
        self.inputdata = InputData.INPUTDATA().hessian_indata(interfacename, casename)
        self.host = self.inputdata['host']
        self.params = self.inputdata['params']
        self.jarname = self.inputdata['jarname']
        self.classname = self.inputdata['classname']
        self.funcname = self.inputdata['funcname']
        self.ruler = HandleDB.HandleDB().db_readruler(interfacename)

    def entity2input(self, entity):
        classname = entity['classname2']
        para = {}
        for k in entity['para']:
            para[k] = {}
            para[k]['value'] = entity['para'][k]['value']
            para[k]['funcname'] = entity['para'][k]['funcname2']
        return classname, para

    def gen_params(self):
        inputpara = {}
        for k in self.params:
            if self.ruler[k]['entity'] == None:
                inputpara[k] = {}
                inputpara[k]['value'] = self.params[k]
                inputpara[k]['funcname'] = self.ruler[k]['funcname1']
            else:
                inputpara[k] = {}
                (classname, para) = self.entity2input(self.ruler[k]['entity'])
                jd = HandleJar.HandleJar().entityjar(self.jarname, para, classname)
                inputpara[k]['value'] = jd
                inputpara[k]['funcname'] = self.ruler[k]['funcname']
        if self.classname == None or self.funcname == None:
            for k in inputpara:
                inputpara[k] = inputpara[k]['value']
            return inputpara
        else:
            entity = HandleJar.HandleJar().entityjar(self.jarname, inputpara, self.classname)
            return entity

    # 访问HESSIAN接口服务器
    def proxy(self, paras):
        proxy = HessianProxy(self.host)
        s = "result = proxy.%s(%s)"%(self.funcname, str(paras))
        exec(s)
        exec ('return result')


def hessian_runner(interfacename, casename):
    p = HESSIAN_REQ(interfacename, casename)
    paras = p.gen_params()
    res = p.proxy(paras)

    return res





if __name__ == '__main__':

    para = HandleJar.HandleJar().valuejar('rrjc-user-api.jar', 'LoginInEntity', '')

