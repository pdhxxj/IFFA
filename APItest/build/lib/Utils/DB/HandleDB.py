#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'


import sys
import MySQLdb
from Common.Exception import HandleException
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
reload(sys)
sys.setdefaultencoding('utf8')


class HandleDB(object):
    def __init__(self):
        self.db_host = '10.10.10.147'
        self.db_user = 'root'
        self.db_passwd = '123456'
        self.db_name = 'funtion'
        self.db_port = 3306

    def db_generaloperation(self, sql):
        try:
            conn = MySQLdb.connect(host=self.db_host,
                                   user=self.db_user,
                                   passwd=self.db_passwd,
                                   db=self.db_name,
                                   port=self.db_port,
                                   charset='utf8' )

            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            return 1
        except Exception, e:
            HandleException.Exception().exception(e)
            return 0

    def db_generalcheck(self,sql,check):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row[0] == check

    def db_readproject(self, projectname):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "select * from project where `projectname`='%s';"%projectname
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        project = {}
        project['projectname'] = row[1]
        project['envname'] = row[2]
        return project

    def db_readtask(self, taskid):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "select `interfacelist`, `projectname` from task where `taskid`=%d"%taskid
        cur.execute(sql)
        row = cur.fetchone()
        projectname = row[1]
        r = eval(row[0])
        print r
        interfacelist = []
        if row == None:
            return None, projectname
        else:
            for k in r:
                interfacelist.append(r[k])
            return interfacelist, projectname

    def db_readenvirement(self, projectname):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "select * from envirement where `projectname`='%s';"%projectname
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        envirement = {}
        envirement['serverip'] = row[2]
        envirement['dbip'] = row[3]
        envirement['dbuser'] = row[4]
        envirement['dbpassword'] = row[5]
        envirement['dbport'] = row[6]
        envirement['isRetry'] = row[8]
        envirement['retrytimes'] = row[9]
        envirement['emaillist'] = row[10]
        return envirement

    def db_readconfig(self, interfacename):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "select * from interface_config where `interfacename`='%s'"%interfacename
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        config = {}
        config['jarname'] = row[1]
        config['classname'] = row[2]
        config['funcname'] = row[3]
        config['projectname'] = row[4]
        config['host'] = row[6]
        config['data'] = row[7]
        config['headers'] = row[8]
        config['method'] = row[9]
        config['cookie'] = row[10]
        config['protocol'] = row[13]
        config['sql_pre'] = row[16]
        config['sql_check'] = row[17]
        config['sql_after'] = row[18]
        return config

    def db_readruler(self, interfacename):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "select %s from interface_config where `interfacename`='%s'" %('ruler', interfacename)
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row[0] == None:
            return None
        else:
            return eval(row[0])

    def db_readexpect(self, interfacename):
        try:
            conn = MySQLdb.connect(host=self.db_host,
                                   user=self.db_user,
                                   passwd=self.db_passwd,
                                   db=self.db_name,
                                   port=self.db_port,
                                   charset='utf8'
                                   )
            cur = conn.cursor()
            sql = "select %s from `interface_config` where `interfacename`='%s'" % ('expect', interfacename)
            cur.execute(sql)
            row = cur.fetchone()
            cur.close()
            conn.close()
            return eval(row[0])
        except Exception,e:
            HandleException.Exception().exception('db_readexpect raise exception:\n' + e)

    def db_writecase(self, interfacename, casename, jarname, classname, funname):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "select * from `case` WHERE `casename`='%s';"%casename
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        if row == None:
            cur = conn.cursor()
            sql = "insert into `case` set casename='%s',`jarname`='%s',`classname`='%s',`funcname`='%s',interfacename='%s',create_time=NOW();" \
                  % (casename,jarname,classname,funname, interfacename)
            cur.execute(sql)
            conn.commit()
            cur.close()
        conn.close()

    def db_readcase(self, interfacename):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "select `casename` from `case` where `interfacename`='%s';"%interfacename
        cur.execute(sql)
        row = cur.fetchall()
        casename = []
        if len(row) >1:
            for i in range(len(row)):
                casename.append(row[i][0])
            return casename
        else:
            casename = row[0][0]
            return casename

    def db_writecaseinfo(self, casename, request, expect_data, jarname, classname, funcname):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "SELECT * from `params` WHERE `casename`='%s';"%casename
        cur.execute(sql)
        row = cur.fetchone()
        if row == None:
            cur = conn.cursor()
            sql = "insert into `params`set casename='%s',`jarname`='%s',`classname`='%s', `funcname`='%s',request='%s', expect='%s',create_time=NOW();" \
                  % (casename,jarname, classname, funcname, request, expect_data)
            cur.execute(sql)
            conn.commit()
            cur.close()
        else:
            cur = conn.cursor()
            sql = "UPDATE `params` set `request`='%s', `expect`='%s' WHERE `casename`='%s';"%(request, expect_data, casename)
            cur.execute(sql)
            conn.commit()
            cur.close()
        conn.close()
        return 1

    def db_readcaseinfo(self, casename):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "SELECT `request` from `params` WHERE `casename`='%s'" %casename
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row[0] != None:
            return eval(row[0])
        else:
            return None

    def db_writeresult(self, taskid, interfacename,jarname, classname, funcname, casename, result, res, error_key, retry, iserror, judge, starttime, endtime, usetime):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "INSERT into result set `taskid`=%d, `interfacename`='%s',`jarname`='%s',`classname`='%s',`funcname`='%s', `casename`='%s',`iserror`='%s',`starttime`='%s',`endtime`='%s',`totaltime`= %f,`totalresult`='%s',`result_body`='%s',`result_headers`='%s',`result_schema`='%s',`result_contenttype`='%s',`result_status`='%s',`realdata`='%s',`error_key`='%s',`retrytimes`='%s',`create_time`=NOW();"\
              %(taskid, interfacename,jarname,classname,funcname,casename, iserror,starttime,endtime,usetime,result, judge['body'], judge['headers'], judge['schema'], judge['content_type'], judge['status_code'],res, error_key,retry)
        cur.execute(sql)
        conn.commit()
        sql2 = "select max(`resultid`) from `result`;"
        cur.execute(sql2)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row[0]

    def db_writecaselog(self, casename, logcache, interfacename, resultid):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "insert into `loginfo` set resultid=%d,interfacename='%s',casename='%s',log='%s',create_time=NOW();"%(resultid, interfacename, casename, logcache)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    def db_writeresponse(self, resultid, response, content_type):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8'
                               )
        cur = conn.cursor()
        sql = "insert into `response` set `resultid`=%d,`body`='%s',`headers`='%s',`content_type`='%s',`status_code`='%s',`cookie`='%s',`create_time`=NOW();"\
              %(resultid, response['req_content'], response['req_headers'], content_type, response['req_status'],response['req_cookie'])
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()


class GeneralDB(object):
    def __init__(self, projectname):
        env = HandleDB().db_readenvirement(projectname)
        self.db_host = env['dbip']
        self.db_user = env['dbuser']
        self.db_passwd = env['dbpassword']
        self.db_port = env['dbport']

    def db_generaloperation(self, sql):
        try:
            conn = MySQLdb.connect(host=self.db_host,
                                   user=self.db_user,
                                   passwd=self.db_passwd,
                                   db=self.db_name,
                                   port=self.db_port,
                                   charset='utf8' )

            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            return 1
        except Exception, e:
            HandleException.Exception().exception(e)
            return 0

    def db_generalcheck(self,sql,check):
        conn = MySQLdb.connect(host=self.db_host,
                               user=self.db_user,
                               passwd=self.db_passwd,
                               db=self.db_name,
                               port=self.db_port,
                               charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row[0] == check


if __name__ == '__main__':

    config = HandleDB().db_readconfig('interface01')
