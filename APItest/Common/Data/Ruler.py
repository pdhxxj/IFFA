#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'
import os
import Yaml
import BaseData
from Utils.Jar import HandleJar
import random
from Common.Exception import HandleException
from Utils.DB import HandleDB


class RULER(object):

    def __init__(self):
        pass

    def config_data(self,interfacename):
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        # 读取config yaml文件
        '''yamlname = parpath + '/Config/interface/' + interfacename + '/' + interfacename + '.yaml'
        config_data = Yaml.YAML().read_yaml(yamlname)'''
        config_data = HandleDB.HandleDB().db_readconfig(interfacename)
        return config_data

    def ruler_data(self, interfacename):
        try:
            path = os.path.dirname(os.getcwd())
            parpath = os.path.dirname(path)
            # 读取config yaml文件
            '''yamlname = parpath + '/Config/interface/' + interfacename + '/' + interfacename + '_r.yaml'
            ruler_data = Yaml.YAML().read_yaml(yamlname)'''
            ruler_data = HandleDB.HandleDB().db_readruler(interfacename)
            return ruler_data
        except Exception,e:
            HandleException.Exception().exception('ruler_data raise exception:\n' + e)

    # 依赖上一个接口返回数据
    def depend_hostdata(self, interfacename, para):
        return 'depend host data test'

    # 生成单个参数数据
    def paradata_int(self, ruler_k):
        single_paradata = []
        if ruler_k['value'] != None:
            paraattr1 = {}
            paraattr1['value'] = ruler_k['value']
            paraattr1['except'] = False
            single_paradata.append(paraattr1)
            return single_paradata
        elif ruler_k['max'] != None and ruler_k['min'] != None:
            # 产生边界值和一个随机等效
            down = ruler_k['min']
            up = ruler_k['max']
            paraattr1 ={}
            paraattr1['value'] = down - 1
            paraattr1['except'] = True
            single_paradata.append(paraattr1)
            paraattr2 = {}
            paraattr2['value'] = up + 1
            paraattr2['except'] = True
            single_paradata.append(paraattr2)
            paraattr3 = {}
            paraattr3['value'] = BaseData.BASEDATA().gen_ranint(down, up)
            paraattr3['except'] = False
            single_paradata.append(paraattr3)
            return single_paradata
        elif ruler_k['max'] != None and ruler_k['min'] == None:
            up = ruler_k['max']
            paraattr1 = {}
            paraattr1['value'] = up + 1
            paraattr1['except'] = True
            single_paradata.append(paraattr1)
            paraattr2 = {}
            paraattr2['value'] = up
            paraattr2['except'] = False
            single_paradata.append(paraattr2)
            return single_paradata
        elif ruler_k['max'] == None and ruler_k['min'] != None:
            down = ruler_k['min']
            paraattr1 = {}
            paraattr1['value'] = down - 1
            paraattr1['except'] = True
            single_paradata.append(paraattr1)
            paraattr2 = {}
            paraattr2['value'] = down
            paraattr2['except'] = False
            single_paradata.append(paraattr2)
            return single_paradata
        else:
            HandleException.Exception().syntaxerror('The paraset is invalid!')

    def paradata_float(self, ruler_k):
        single_paradata = []
        if ruler_k['value'] != None:
            paraattr1 = {}
            paraattr1['value'] = ruler_k['value']
            paraattr1['except'] = False
            single_paradata.append(paraattr1)
            return single_paradata
        elif ruler_k['max'] != None and ruler_k['min'] != None:
            # 产生边界值和一个随机等效
            down = ruler_k['min']
            up = ruler_k['max']
            paraattr1 = {}
            paraattr1['value'] = down - 0.01
            paraattr1['except'] = True
            single_paradata.append(paraattr1)
            paraattr2 = {}
            paraattr2['value'] = up + 0.01
            paraattr2['except'] = True
            single_paradata.append(paraattr2)
            paraattr3 = {}
            paraattr3['value'] = BaseData.BASEDATA().gen_ranfloat(down, up)
            paraattr3['except'] = False
            single_paradata.append(paraattr3)
            return single_paradata
        elif ruler_k['max'] != None and ruler_k['min'] == None:
            up = ruler_k['max']
            paraattr1 = {}
            paraattr1['value'] = up + 0.01
            paraattr1['except'] = True
            single_paradata.append(paraattr1)
            paraattr2 = {}
            paraattr2['value'] = up
            paraattr2['except'] = False
            single_paradata.append(paraattr2)
            return single_paradata
        elif ruler_k['max'] == None and ruler_k['min'] != None:
            down = ruler_k['min']
            paraattr1 = {}
            paraattr1['value'] = down - 0.01
            paraattr1['except'] = True
            single_paradata.append(paraattr1)
            paraattr2 = {}
            paraattr2['value'] = down
            paraattr2['except'] = False
            single_paradata.append(paraattr2)
            return single_paradata
        else:
            HandleException.Exception().syntaxerror('The paraset is invalid!')

    def paradata_context(self, ruler_k):
        single_paradata = []
        paraattr = {}
        if ruler_k['value'] != None:
            paraattr['value'] = ruler_k['value']
            paraattr['except'] = False
            single_paradata.append(paraattr)
            return single_paradata
        elif ruler_k['long'] != None:
            long = ruler_k['long']
            paraattr['value'] = BaseData.BASEDATA().gen_rancontext(long)
            paraattr['except'] = False
            single_paradata.append(paraattr)
            return single_paradata
        else:
            HandleException.Exception().syntaxerror('The paraset is invalid!')


    def paradata_bool(self, ruler_k):
        single_paradata = []
        paraattr = {}
        if ruler_k['value'] != None:
            paraattr['value'] = ruler_k['value']
            paraattr['except'] = False
            single_paradata.append(paraattr)
            return single_paradata
        else:
            HandleException.Exception().syntaxerror('The paraset is invalid!')

    def paradata_json(self, ruler_k):
        single_paradata = []
        paraattr = {}
        if ruler_k['value'] != None:
            paraattr['value'] = ruler_k['value']
            paraattr['except'] = False
            single_paradata.append(paraattr)
            return single_paradata
        else:
            HandleException.Exception().syntaxerror('The paraset is invalid!')

    def paradata_list(self, ruler_k):
        single_paradata = []
        if ruler_k['value'] != None:
            for i in range(len(ruler_k['value'])):
                paraattr = {}
                paraattr['value'] = ruler_k['value'][i]
                paraattr['except'] = False
                single_paradata.insert(i, paraattr)
            return single_paradata
        else:
            HandleException.Exception().syntaxerror('The paraset is invalid!')

    def paradata_jar(self, entity):

        single_paradata = []
        paraattr = {}
        paraattr['value'] = entity
        paraattr['except'] = False
        single_paradata.append(paraattr)
        return single_paradata



if __name__ == '__main__':
    ruler_k = {'type': 'list',
               'value': [1,2,3,4,5],
               'long': None,
               'max': None,
               'min': None,
               'notnull': True,
               'jar': {'jartype': 'object',
                       'jarname': 'test.jar',
                       'jarpara': {},
                       'classname': '',
                       'funcname': ''
                    }
               }

    result = RULER().paradata_list(ruler_k)
    print result