#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

__author__ = '小今今'
from distutils.core import setup

setup(
    name='IFFA',
    version='1.0',
    packages=['APItest','APItest.Common','APItest.Config','APItest.Core','APItest.Report','APItest.TestCase','APItest.Utils','APItest.Common.Assert', 'APItest.Common.Data','APItest.Common.Exception','APItest.Common.Log',
              'APItest.Common.Mock','APItest.Common.Retry','APItest.Common.Runner','APItest.Config.Lib','APItest.Config.Other',
              'APItest.Core.Http','APItest.Core.Https','APItest.Core.Response','APItest.Report.Html','APItest.Report.Result',
              'APItest.TestCase.BuildCase','APItest.Utils.DB','APItest.Utils.Email','APItest.Utils.File','APItest.Utils.Jar'],
    license='1.0',
    author='小今今',
    author_email='gjperfect@163.com',
    description=''
)