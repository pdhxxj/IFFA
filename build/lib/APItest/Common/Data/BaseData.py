#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'
import random
import string
from Utils import Md5
import jpype
import os
from Common.Exception import HandleException
from Utils.Jar import HandleJar
'''
基础数据处理
'''


class BASEDATA(object):

    def __init__(self):
        pass

    def gen_rancontext(self, long):
        salt = ''.join(random.sample(string.ascii_letters + string.digits, long))
        return salt

    def gen_arancontext(self):
        salt = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(0,20)))
        return salt

    def gen_ranfloat(self, down, up):
        salt = random.uniform(down, up)
        return salt

    def gen_rannum(self, long):
        salt = ''.join(random.sample(string.digits, long))
        return salt

    def gen_arannum(self):
        salt = ''.join(random.sample(string.digits, random.randint(0, 20)))
        return salt

    def gen_ranstr(self, long):
        salt = ''.join(random.sample(string.ascii_letters, long))
        return salt

    def gen_aranstr(self):
        salt = ''.join(random.sample(string.ascii_letters, random.randint(0, 20)))
        return salt

    def gen_ranint(self, down, up):
        num = random.randint(down, up)
        return num

    def gen_id(self):
        pass

    def gen_telephone(self):
        pass

    def gen_phone(self):
        pass

    def judge_enum(self, enum):
        if type(enum) == 'list':
            return True
        else:
            return False

    def judge_group(self, group):
        if '[' in str(group):
            return True
        else:
            return False

    def get_md5(self, s):
        result = Md5.MD5().get_smd5(s)
        return result

