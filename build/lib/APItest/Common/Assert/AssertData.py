#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

from Common.Exception import  HandleException
from Core.Response import handleresponse
import schema
from Utils.DB import HandleDB


class ASSERTDATA(object):

    def __init__(self):
        pass

    def judge_responsetype(self):
        pass


    # 获取实际待对比http返回数据
    def get_responsedata(self, res,tag):
        if tag == 1:
            res_data = handleresponse.HANDLERESPONSE().handle_httpres(res)
            return res_data
        else:
            HandleException.Exception().syntaxerror('The expect tag is invalid!')


    def assert_hessiandata(self, res, expect_data):
        error_key = {}
        judge = {'body': None,
                 'headers': None,
                 'schema': None,
                 'content_type': None,
                 'status_code': None
                 }
        if expect_data != None and res != None:
            for k in expect_data:
                expect = expect_data[k]
                if expect['type'].lower() == 'obj' and expect['entity'] != None:
                    checkpart = handleresponse.HANDLERESPONSE().handle_resentity(expect['entity'], res[k])

    def assert_data(self, res, expect_data):
        error_key = {}
        judge = {'body': None,
                 'headers': None,
                 'schema': None,
                 'content_type': None,
                 'status_code': None
                 }
        if res != None and expect_data != None:
            if expect_data['body']['ischeck'] == True:
                for k in expect_data['body']['value']:
                    if res['req_content'] == None or res['req_headers']['Content-Type'] != 'application/json':
                        judge['body'] = 'Not Run'
                    elif eval(res['req_content']).has_key(k) == False:
                        judge['body'] = False
                        error_key[k] = 'Loss'
                    elif res['req_content'][k] != expect_data['body']['value'][k] and isinstance(expect_data['body']['value'][k], dict):
                        judge['body'] = False
                        error_key[k] = 'Key Error'
                    else:
                        judge['body'] = True
                        continue
            else:
                judge['body'] = 'Not Judge'
            if expect_data.has_key('headers'):
                if expect_data['headers']['ischeck'] == True:
                    if res['req_headers'] == None:
                        judge['headers'] = 'Not Run'
                    elif res['req_headers'] != expect_data['headers']['value']:
                        judge['headers'] = False
                    else:
                        judge['headers'] = True
                else:
                    judge['headers'] = 'Not Judge'
            if expect_data.has_key('schema'):
                if expect_data['schema']['ischeck'] == True:
                    if res['req_headers']['Content-Type'] == 'application/json':
                        model = expect_data['schema']['value']
                        validate = res['req_content']
                        try:
                            result = schema.Schema(model).validate(validate)
                            judge['schema'] = True
                        except Exception:
                            judge['schema'] = False
                    else:
                        judge['schema'] = False
                else:
                    judge['schema'] = 'Not Judge'
            if expect_data.has_key('schema'):
                if expect_data['content_type']['ischeck'] == True:
                    if res['req_headers'] == None:
                        judge['content_type'] = 'Not Run'
                    elif res['req_headers']['Content-Type'] == None:
                        judge['content_type'] = 'Not Run'
                    elif expect_data['content_type']['value'] != res['req_headers']['Content-Type']:
                        judge['content_type'] = False
                        error_key['content_type'] = 'Key Error'
                    else:
                        judge['content_type'] = True
                else:
                    judge['content_type'] = 'Not Judge'
                if res['req_status'] == 200:
                    judge['status_code'] = True
                else:
                    judge['status_code'] = False
        else:
            judge = {'body': 'Not Run',
                     'headers': 'Not Run',
                     'schema': 'Not Run',
                     'content_type': 'Not Run',
                     'status_code': 'Not Run'
                     }
        # 判定总结果
        result = 'Not Run'
        error_key['respose&expect'] = 'Response or Expect is null'
        for k in judge:
            if judge[k] != True:
                result = 'fail'
                break
            else:
                result = 'pass'
                continue
        return judge, error_key, result

    def assert_runner(self, res, expect_data):
        # (res_data, res_status) = self.get_responsedata(res, expectpart, tag)

        (judge, error_key,result) = self.assert_data(res, expect_data)
        return judge, error_key, result

    # 先写在这里
    def assert_runnerhessian(self, res, expect_data):
        (judge, error_key,result) = self.assert_hessiandata(res, expect_data)
        return judge, error_key, result



class ASSERTDATABASE(object):
    def __index__(self):
            pass

    def assert_database(self, config_data):
        # 校验数据库
        sql_check = eval(config_data['sql_check'])
        if sql_check != None:
            sql = sql_check['sql']
            check = sql_check['check']
            result = HandleDB.HandleDB().db_generalcheck(sql, check)
            return result
        else:
            return 'error'







