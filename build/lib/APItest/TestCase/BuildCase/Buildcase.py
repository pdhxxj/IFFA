#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

from Common.Data import Combination
from Common.Data import Ruler
from Common.Data import Yaml
from Common.Exception import HandleException
from Utils.File import File
from Common.Data import  Txt
import os
import json
from Utils.DB import HandleDB


class BUILDCASE(object):

    def __init__(self):
        pass

    # 拼出每个参数产生的值
    def gen_paradata(self, ruler_data):
        try:
            if ruler_data != None:
                gen_params = {}
                for k in ruler_data:
                    if ruler_data[k]['type'].lower() == 'number':
                        gen_params[k] = Ruler.RULER().paradata_int(ruler_data[k])
                    elif ruler_data[k]['type'].lower() == 'float':
                        gen_params[k] = Ruler.RULER().paradata_float(ruler_data[k])
                    elif ruler_data[k]['type'].lower() == 'string':
                        gen_params[k] = Ruler.RULER().paradata_context(ruler_data[k])
                    elif ruler_data[k]['type'].lower() == 'bool':
                        gen_params[k] = Ruler.RULER().paradata_bool(ruler_data[k])
                    elif ruler_data[k]['type'].lower() == 'json':
                        gen_params[k] = Ruler.RULER().paradata_bool(ruler_data[k])
                    elif ruler_data[k]['type'].lower() == 'list':
                        gen_params[k] = Ruler.RULER().paradata_float(ruler_data[k])
                    elif ruler_data[k]['type'].lower() == 'obj':
                        entity = ruler_data[k]['entity']
                        gen_params[k] = Ruler.RULER().paradata_jar(entity)
                    else:
                        HandleException.Exception().syntaxerror('The paratype of %s is invalid' %k)
            else:
                gen_params = None
            return gen_params
        except Exception,e:
            HandleException.Exception().exception('gen_paradata raise exception:\n'+ e)

    # 入参数据写入case表
    def gen_case(self, paradata, interfacename, casenum, expect_data, jarname, classname, funname):
        try:
            if funname != None:
                interfacename2 = interfacename + '_' + funname
                casename = interfacename2+casenum
            else:
                casename = interfacename + casenum
            HandleDB.HandleDB().db_writecase(interfacename, casename, jarname, classname, funname)
            if paradata == None:
                paradata = 'None'
            else:
                paradata = json.dumps(paradata,ensure_ascii=False)
            expect_data = json.dumps(expect_data, ensure_ascii=False)
            HandleDB.HandleDB().db_writecaseinfo(casename, paradata, expect_data, jarname, classname, funname)
        except Exception,e:
            HandleException.Exception().exception('gen_case raise exception:\n' + e)

    def gen_lackcase(self, paradata, interfacename, expect_data, jarname, classname, funname):
        try:
            if funname != None:
                interfacename2 = interfacename + '_' + funname
                casename = interfacename2+'_lack'
            else:
                casename = interfacename + '_lack'
            HandleDB.HandleDB().db_writecase(interfacename, casename,jarname, classname, funname)
            paradata = json.dumps(paradata, ensure_ascii=False)
            expect_data = json.dumps(expect_data, ensure_ascii=False)
            HandleDB.HandleDB().db_writecaseinfo(casename, paradata, expect_data, jarname, classname, funname)
        except Exception,e:
            HandleException.Exception().exception('gen_lackcase raise exception:\n' + e)

    # 生成case文件
    def gen_testcase(self, interfacename, gen_params, expect_data, ruler_data, jarname, classname, funname):
        paramslist = gen_params
        case_error = {}
        # 用allpairs产生用例合集
        if paramslist != None:
            if len(paramslist) > 1:
                caselist1 = Combination.ITER().allpairs(paramslist)
                lackpara = Combination.ITER().lackpara(paramslist, ruler_data)
                self.gen_lackcase(lackpara, interfacename, expect_data, jarname, classname, funname)
                case_error[interfacename + '_lack'] = None
            # 单个参数
            else:
                caselist1 = []
                for k in paramslist:
                    para = paramslist[k]
                    for i2 in range(len(para)):
                        single_para = {}
                        single_para[k] = para[i2]['value']
                        single_para['error'] = para[i2]['except']
                        caselist1.append(single_para)

            for i in range(len(caselist1)):
                casenum = i+1
                in_paradata = caselist1[i]
                error = in_paradata['error']
                del in_paradata['error']
                self.gen_case(in_paradata, interfacename, str(casenum), expect_data, jarname, classname, funname)
                case_error[interfacename+str(casenum)] = error
        else:
            case_error = {}
            self.gen_case(paradata=None, interfacename=interfacename, casenum='_NonePara', expect_data=expect_data,
                          jarname=jarname, classname=classname, funname=funname)
            case_error[interfacename+'_NonePara'] = None
        return case_error

if __name__ == '__main__':
    gen_params = BUILDCASE().gen_paradata('httpbin')
    BUILDCASE().gen_testcase('httpbin', gen_params)




