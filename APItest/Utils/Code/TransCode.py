#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import chardet
from Common.Log import Log


class TransCode(object):
    def __init__(self):
        pass

    # 只对string流对象有用
    def transcode(self, strobject):
        result = chardet.detect(strobject)
        coding = result.get('encoding')
        Log.LOG('case coding type').log_result(coding)
        new = strobject.decode('GBK').encode('UTF-8')
        return new
