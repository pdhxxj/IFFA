#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import jpype
import os


class HandleJar(object):
    def __init__(self):
        pass

    def entityjar(self, jarname, params, classname):
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        jarpath = parpath + '/Config/Lib/%s'%jarname
        jvmArg = "-Djava.class.path=" + jarpath
        print jvmArg
        jvmPath = jpype.getDefaultJVMPath()
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, '-ea', jvmArg)
        JDClass = jpype.JClass(classname)
        jd = JDClass()
        # params必须以字典方式写入
        for k in params:
            para = params[k]['value']
            func = params[k]['funcname']
            if isinstance(para, str):
                s = "jd.%s('%s')"%(func, str(para))
            else:
                s = "jd.%s(%s)"%(func, str(para))
            exec(s)
        jpype.shutdownJVM()
        return jd

    def valuejar(self, jarname, classname, jarfuncname, params=None):
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        jarpath = parpath + '/Config/Lib/%s' % jarname
        jvmArg = "-Djava.class .path =" + jarpath
        jvmPath = jpype.getDefaultJVMPath()
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, '-ea', jvmArg)
        jd = jpype.JClass(classname)
        s = 'result = jd.%s(' % jarfuncname

        if isinstance(params, str):
            s = s + "'%s')"%params
            exec(s)
            exec('return result')
        else:
            s = s + "%s)" % params
            exec (s)
            exec ('return result')
        jpype.shutdownJVM()


if __name__ == '__main__':
    def getclass():
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        jarpath = parpath + '/Config/Lib/hello.jar'
        jvmArg = "-Djava.class.path=" + jarpath
        jvmPath = jpype.getDefaultJVMPath()
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, '-ea', jvmArg)
        JDClass = jpype.JClass('com.test.hello.Hello')
        jd = JDClass()
        jd.setEmail('hahahaha')
        jd.setId(8)
        jpype.shutdownJVM()
        return jd

    obj1 = 8
    path = os.path.dirname(os.getcwd())
    parpath = os.path.dirname(path)
    jarpath = parpath + '/Config/Lib/parse_entity.jar'
    jvmArg = "-Djava.class.path=" + jarpath
    jvmPath = jpype.getDefaultJVMPath()
    if not jpype.isJVMStarted():
        jpype.startJVM(jvmPath, '-ea', jvmArg)
    JDClass = jpype.JClass('com.test.parse_entity.ParseEntity')
    p = JDClass()
    result = p.parse(obj1)
    jpype.shutdownJVM()
    print type(result)
    resutl = str(result)
    print result

