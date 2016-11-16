#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import yaml
from Utils.File import File
import os
from Common.Exception import HandleException
import codecs


class YAML(object):

    def __init__(self):
        pass

    # 读取interface.yaml文件
    def read_yaml(self, yamlname):
        with codecs.open(yamlname, 'r', 'utf-8')as f:
            stream = f.read()
            yaml_data = yaml.load(stream)
        return yaml_data

    def write_yaml(self, yamlname, ydata):
        with codecs.open(yamlname, 'w', 'utf-8')as f:
            yaml.dump(yaml.load(ydata), f)

