#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

from Common.Log import Log


class Exception(object):

    def __init__(self):
        pass

    def exception(self, e):
        # 打印代码内部错误
        Log.LOG('Program error').log_error(e)

    def syntaxerror(self, s):
        try:
            raise SyntaxError
        except SyntaxError:
            Log.LOG('Syntax Error').log_error(s)

    def systemerror(self, s):
        try:
            raise SystemError
        except SystemError:
            Log.LOG('System Error').log_error(s)


