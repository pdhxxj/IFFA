#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

from pyh import *
import os
from Utils.File import File
import json

class StaticResult(object):
    def __init__(self):
        pass

    def staticresult(self, report_case):
        succtime = 0
        failtime = 0
        for k in report_case:
            if report_case[k]['judge'] == True:
                succtime += 1
            else:
                failtime += 1
        return succtime, failtime


class BuildHtml(object):

    def __init__(self):
        pass

    def build_funcreport(self, interfacename, report_case,expectdata):
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        cssdir = parpath + '/Report/Html/reporthome.css'
        (succtime, failtime) = StaticResult().staticresult(report_case)

        page = PyH('Function Test Report')
        page.addCSS(cssdir)
        page << h1('%s funtion report'%interfacename, cl='center', align='center')
        page << br('')
        page << div('The total case: %d'%len(report_case)) + div('The success case: %d'%succtime) + div('The fail case: %d'%failtime)
        page += div('The test result is:') << br('')
        tab = table(cl='hovertable')
        tab << tr(onmouseover="this.style.backgroundColor='#ffff66';", onmouseout="this.style.backgroundColor='#d4e3e5';",charset='gb2312')
        tab << th('CaseName') + th('RunResult') + th('TotalResult') + th('Diff') + th('UseTime')
        #循环切入点
        for k in report_case:
            tab += tr(onmouseover="this.style.backgroundColor='#ffff66';", onmouseout="this.style.backgroundColor='#d4e3e5';", charset='gb2312')
            tab << td('%s'%k) + td('%s'%str(report_case[k]['judge'])) + td('%s'%str(report_case[k]['result'])) \
                   + td(' ') + td(report_case[k]['usetime'])
        page << tab
        filename = parpath + '/Report/Html/%s/'%interfacename
        if os.path.exists(filename) == False:
            File.FILE().make_dir(filename)
        page.printOut(filename+interfacename + '_func.html')


