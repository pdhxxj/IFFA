#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import unittest
import HTMLTestRunner
import os
from Common.Exception import HandleException


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param
    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


class TestOne(ParametrizedTestCase):
    def testcase(self):
        self.assertEqual(self.param, True, 'Test Error')


class BuildHtmlReport(object):

    def __init__(self):
        pass

    def gen_htmlreport(self, interfacename, runsuite):
        try:
            path = os.path.dirname(os.getcwd())
            parpath = os.path.dirname(path)
            filename = parpath + '/Report/Html/%s_report.html'%interfacename
            with open(filename, 'wb')as f:
                runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='%s Test Report'%interfacename,
                                                       description='This  is %s Test  Report'%interfacename)
                runner.run(runsuite)
        except Exception, e:
            HandleException.Exception().exception(e)
