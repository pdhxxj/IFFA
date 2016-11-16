#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import logging
from logging.handlers import RotatingFileHandler
import sys
import os


# 防重复参考
def log(message):
    logger = logging.getLogger('testlog')

    #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        streamhandler.setFormatter(formatter)
        logger.addHandler(streamhandler)

    logger.error(message)


class LOG(object):
    def __init__(self, tag='default'):
        self.tag = tag
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        # 构造日志存放路径
        path = os.path.dirname(os.getcwd())
        parpath = os.path.dirname(path)
        self.path = parpath + '/Report/Result/'

    def log_debug(self, msg):
        logger = logging.getLogger(self.tag)
        if not logger.handlers:
            # hdlr = logging.FileHandler(os.path.join(os.getcwd(), self.path + 'loginfo.log'), 'a+')
            hdlr = RotatingFileHandler(os.path.join(os.getcwd(), self.path + 'logdebug.log'),
                                       'a+',
                                       maxBytes=1 * 1024 * 1024,
                                       backupCount=8)
            hdlr.setFormatter(self.formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.DEBUG)
            logger.debug(msg)
            logger.removeHandler(hdlr)

    def log_warning(self, msg):
        logger = logging.getLogger(self.tag)
        if not logger.handlers:
            # hdlr = logging.FileHandler(os.path.join(os.getcwd(), self.path + 'loginfo.log'), 'a+')
            hdlr = RotatingFileHandler(os.path.join(os.getcwd(), self.path + 'logwarning.log'),
                                       'a+',
                                       maxBytes=1 * 1024 * 1024,
                                       backupCount=8)
            hdlr.setFormatter(self.formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.WARNING)
            logger.warning(msg)
            logger.removeHandler(hdlr)

    def log_error(self, msg):
        logger = logging.getLogger(self.tag)
        if not logger.handlers:
            # hdlr = logging.FileHandler(os.path.join(os.getcwd(), self.path + 'loginfo.log'), 'a+')
            hdlr = RotatingFileHandler(os.path.join(os.getcwd(), self.path + 'logerror.log'),
                                       'a+',
                                       maxBytes=1 * 1024 * 1024,
                                       backupCount=8)
            hdlr.setFormatter(self.formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.ERROR)
            logger.error(msg)
            logger.removeHandler(hdlr)

    def log_info(self, msg):
        logger = logging.getLogger(self.tag)
        if not logger.handlers:
            # hdlr = logging.FileHandler(os.path.join(os.getcwd(), self.path + 'loginfo.log'), 'a+')
            hdlr = RotatingFileHandler(os.path.join(os.getcwd(), self.path + 'loginfo.log'),
                                                        'a+',
                                                        maxBytes=1*1024*1024,
                                                        backupCount=8)
            hdlr.setFormatter(self.formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.INFO)
            logger.info(msg)
            logger.removeHandler(hdlr)

    def log_result(self, msg):
        logger = logging.getLogger(self.tag)
        if not logger.handlers:
            # hdlr = logging.FileHandler(os.path.join(os.getcwd(), self.path + 'loginfo.log'), 'a+')
            hdlr = RotatingFileHandler(os.path.join(os.getcwd(), self.path + 'logresult.log'),
                                                        'a+',
                                                        maxBytes=1*1024*1024,
                                                        backupCount=8)
            hdlr.setFormatter(self.formatter)
            logger.addHandler(hdlr)
            logger.setLevel(logging.INFO)
            logger.info(msg)
            logger.removeHandler(hdlr)



