#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

from Common.Data import InputData
from Common.Assert import  AssertData
from Core.Http import Http
from Core.Https import Https
from Core.Hessian import Hessian
from TestCase.BuildCase import Buildcase
from Common.Log import Log
from Common.Exception import HandleException
from Common.Data import Ruler
from Utils.DB import HandleDB
import os
import time
import json
import sys
from Utils.Email import SendEmail


# 跑一次单个接口单个情况
class FUNCTION(object):

    def __init__(self):
        self.r = AssertData.ASSERTDATA()

    def build_case(self, interfacename, expect_data, ruler_data, jarname, classname, funname):
        gen_params = Buildcase.BUILDCASE().gen_paradata(ruler_data)
        case_error = Buildcase.BUILDCASE().gen_testcase(interfacename, gen_params, expect_data, ruler_data, jarname, classname, funname)
        return case_error

    def all_case(self, interfacename):
        try:
            start = time.clock()
            '''path = os.path.dirname(os.getcwd())
            parpath = os.path.dirname(path)
            dirname = parpath + '/TestCase/Function/' + interfacename'''
            casename = HandleDB.HandleDB().db_readcase(interfacename)
            end = time.clock()
            Log.LOG(interfacename).log_result('The case of %s has built using %s'%(interfacename, str(end - start)))
            Log.LOG(interfacename).log_result('The caselist is:\n %s'%str(casename))
            return casename
        except Exception,e:
            HandleException.Exception().exception('all_case raise exception:\n'+ e)

    def sql_preoperation(self, sql):
        if sql != None:
            finish = HandleDB.HandleDB().db_generaloperation(sql)
        else:
            finish = 1
        return finish

    def run_onetime(self, interfacename, casename, config_data, expect_data,):
        '''
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        yamlname = parpath + '/Config/interface/' + '%s/%s.yaml' % (interfacename, interfacename)
        config_data = Yaml.YAML().read_yaml(yamlname)'''
        try:
            start = time.clock()
            if config_data['protocol'].lower() == 'http':
                res = Http.http_runner(interfacename, casename)
                end = time.clock()
                Log.LOG(interfacename + '->' + casename).log_result('Http has get the response data using %s'%str(end - start))
                logcache = '%s--->%s: Http has get the response data using %s\n'%(interfacename, casename, str(end - start))
                (judge, error_key, result) = self.r.assert_runner(res, expect_data)
                return judge, error_key, logcache, res, round((end - start),2), result
            elif config_data['protocol'].lower() == 'https':
                res = Https.https_runner(interfacename, casename)
                end = time.clock()
                Log.LOG(interfacename + '->' + casename).log_result('Https has get the response data using %s' % str(end - start))
                logcache = '%s--->%s: Http has get the response data using %s\n'%(interfacename, casename, str(end - start))
                (judge, error_key, result) = self.r.assert_runner(res, expect_data)
                return judge, error_key, logcache, res, round((end - start),2), result
            elif config_data['protocol'].lower() == 'hessian':
                res = Hessian.hessian_runner(interfacename, casename)
                end = time.clock()
                Log.LOG(interfacename + '->' + casename).log_result('Hessian has get the response data using %s' % str(end - start))
                logcache = '%s--->%s: Http has get the response data using %s\n'%(interfacename, casename, str(end - start))
                (judge, error_key,result) = self.r.assert_runnerhessian(res, expect_data)
                return judge, error_key, logcache, res, round((end - start),2), result
            else:
                HandleException.Exception().syntaxerror('The interface type is not exist! ')
        except Exception,e:
            HandleException.Exception().exception(e)

    def run_singlecase(self, interfacename, casename, config_data, expect_data, projectname):
        try:
            # 测试前数据库操作
            sql = config_data['sql_pre']
            finish = self.sql_preoperation(sql)
            env = HandleDB.HandleDB().db_readenvirement(projectname)
            retry = env['isRetry']
            wholetime = 0.00
            if finish != 1:
                runtime = env['retrytimes']
                judge = False
                error_key = 'Pre Sql Operation cannot pass !'
                res_data = ''
                logcache2 = '%s--->%s: %s'%(interfacename, casename, error_key)
            else:
                runtime = 0
                logcache2 = ''
            while runtime < env['retrytimes'] and retry == True:
                (judge, error_key, logcache, res, usetime, result) = self.run_onetime(interfacename, casename, config_data, expect_data)
                wholetime += usetime
                if judge != True:
                    Log.LOG(interfacename + '->' + casename).log_result('Run fail %d times,The error: \n %s'%(runtime+1, str(error_key)))
                    logcache = logcache + '%s-->%s: Run fail %d times,The error: \n %s'%(interfacename, casename, runtime+1, str(error_key)) + '\n'
                else:
                    Log.LOG(interfacename + '->' + casename).log_result('Run success')
                    Log.LOG(interfacename + '->' + casename).log_result('The check data: \n %s'%res_data)
                    logcache = logcache + '%s-->%s: Run success\n The check data: \n %s'%(interfacename, casename, res_data) + '\n'
                    # 若通过不再重跑
                    runtime = env['retrytimes']
                logcache2 += logcache
                runtime += 1
            if retry != True:
                (judge, error_key, logcache, res, usetime, result) = self.run_onetime(interfacename, casename, config_data, expect_data)
                wholetime += usetime
                if judge != True:
                    Log.LOG(interfacename + '->' + casename).log_result('Run fail %d times,The error: \n %s' % (runtime + 1, str(error_key)))
                    logcache = logcache + '%s-->%s: Run fail %d times,The error: \n %s' % (
                    interfacename, casename, runtime + 1, str(error_key)) + '\n'
                else:
                    Log.LOG(interfacename + '->' + casename).log_result('Run success')
                    Log.LOG(interfacename + '->' + casename).log_result('The check data: \n %s' % res_data)
                    logcache = logcache + '%s-->%s: Run success\n The check data: \n %s' % (
                    interfacename, casename, res_data) + '\n'
                logcache2 += logcache
                runtime += 1
            return judge, error_key, runtime, logcache2, res, wholetime, result
        except Exception,e:
            HandleException.Exception().exception(e)

    def run_singleinterface(self, interfacename, taskid):
        # 建立case
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        start = time.clock()
        # 取配置值
        config_data = InputData.INPUTDATA().get_configdata(interfacename)
        jarname = config_data['jarname']
        classname = config_data['classname']
        funcname = config_data['funcname']
        projectname = config_data['projectname']
        ruler_data = Ruler.RULER().ruler_data(interfacename)
        Log.LOG(interfacename).log_result('The config data of %s:\n%s'%(interfacename, str(config_data)))
        # 取期望值
        expect_data = HandleDB.HandleDB().db_readexpect(interfacename)
        case_error = self.build_case(interfacename, expect_data, ruler_data, jarname, classname, funcname)
        Log.LOG(interfacename).log_result('The case of %s build success...' %interfacename)
        casename = self.all_case(interfacename)
        print type(casename)
        report_case = {}
        # 如果不是无参接口
        if ruler_data != None and isinstance(casename, list):
            for i in range(len(casename)):
                starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    (judge, error_key, runtimes, logcache2, res, usetime,result) = self.run_singlecase(interfacename,
                                                                                                       casename[i],
                                                                                                       config_data,
                                                                                                       expect_data,
                                                                                                       projectname)
                    realvalue = str(res).replace("'", "\"")
                    # realvalue = json.dumps(realvalue, ensure_ascii=False)
                    # print realvalue, type(realvalue)
                    error_key = json.dumps(error_key, ensure_ascii=False)
                    logcache = str(logcache2).replace("'", "\"")
                    # 处理res 写进response表
                    content_type = str(res['req_headers']['Content-Type'])
                    for k in res:
                        if k == 'req_headers':
                            res[k] = str(res[k]).replace("'", "\"")
                except Exception,e:
                    res = {"req_status": 999,
                                "req_headers": None,
                                "req_content": None,
                                "req_token": None,
                                "req_cookie": None
                                }
                    HandleException.Exception().exception(str(casename[i]) + 'raise exception:\n' + e)
                    judge = {"body": None, "headers": None, "schema": None, "content_type": None, "status_code": None}
                    error_key = None
                    runtimes = 0
                    logcache = None
                    realvalue = None
                    result = 'Not Run'
                    content_type = None
                    usetime = 'Unknown'
                iserror = case_error[casename[i]]
                endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                resultid = HandleDB.HandleDB().db_writeresult(taskid, interfacename, jarname, classname, funcname, casename[i], result, realvalue, error_key,
                                                              str(runtimes-1), iserror, judge, starttime, endtime, usetime)
                HandleDB.HandleDB().db_writecaselog(casename[i], logcache, interfacename, resultid)
                HandleDB.HandleDB().db_writeresponse(resultid, res, content_type)
                report_case[casename[i]] = {'result': result, 'judge': judge, 'usetime': usetime}
        else:
            starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            try:
                (judge, error_key, runtimes, logcache2, res, usetime,result) = self.run_singlecase(interfacename, casename,
                                                                                        config_data, expect_data,
                                                                                        projectname)

                realvalue = str(res).replace("'", "\"")
                error_key = json.dumps(error_key, ensure_ascii=False)
                # 设置一个存储日志内容的变量,将'替换成*号
                logcache = str(logcache2).replace('\'', '*')
                content_type = str(res['req_headers']['Content-Type'])
                for k in res:
                    if k == 'req_headers':
                        res[k] = str(res[k]).replace("'", "\"")
            except Exception,e:
                res = {"req_status": 999,
                       "req_headers": None,
                       "req_content": None,
                       "req_token": None,
                       "req_cookie": None
                       }
                HandleException.Exception().exception(casename + 'raise exception:\n' + e)
                judge = {"body": None, "headers": None, "schema": None, "content_type": None, "status_code": None}
                error_key = None
                runtimes = 0
                logcache = None
                realvalue = None
                result = 'Not Run'
                content_type = None
                usetime = 'Unknown'
            iserror = case_error[casename]
            endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            resultid = HandleDB.HandleDB().db_writeresult(taskid, interfacename, jarname, classname, funcname, casename, result, realvalue, error_key,
                                                              str(runtimes-1), iserror, judge, starttime, endtime, usetime)
            HandleDB.HandleDB().db_writecaselog(casename, logcache, interfacename, resultid)
            HandleDB.HandleDB().db_writeresponse(resultid, res, content_type)
            report_case[casename] = {'result': result, 'judge': judge, 'usetime': usetime}
            # testsuite.addTest(Html.ParametrizedTestCase.parametrize(Html.TestOne, param=judge))
        # BuildHtml.BuildHtml().build_funcreport(interfacename, report_case, expect_data)
        # 将每个case加载到报告中
        # Html.BuildHtmlReport().gen_htmlreport(interfacename, testsuite)
        end = time.clock()
        # 数据库收尾处理
        sql = config_data['sql_after']
        if sql != None:
            finish = HandleDB.HandleDB().db_generaloperation(sql)
        else:
            finish = 1
        if finish == 1:
            Log.LOG(interfacename).log_result('The %s end running------------------' % interfacename)
            Log.LOG(interfacename).log_result('The whole time of running %s is %s' % (interfacename, str(end-start)))
        else:
            Log.LOG(interfacename).log_result('The after sql operation is unfinished!')

    def run_task(self, taskid):
        # 读取interfacelist
        (interfacelist, projectname) = HandleDB.HandleDB().db_readtask(taskid)
        if interfacelist == None:
            emailcontent = 'The task set is None ,can not run!'
        else:
            for i in range(len(interfacelist)):
                self.run_singleinterface(interfacelist[i], taskid)
            emailcontent = 'The taskid %d has finished'%taskid
        envirement = HandleDB.HandleDB().db_readenvirement(projectname)
        emaillist = eval(envirement['emaillist'])
        SendEmail.SendEmail().sendemail(emaillist, emailcontent)

if __name__ == '__main__':
    taskid = sys.argv[0]
    r = FUNCTION()
    r.run_task(1)





















