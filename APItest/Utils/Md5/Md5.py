#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import hashlib

'''
获取md5值
'''


class MD5(object):

    def get_fmd5(self, filename):
        m = hashlib.md5()
        with open(filename, 'rb')as f:
            f = f.read()
            m.update(f)
        result = m.hexdigest()
        return result

    def get_smd5(self, s):
        m = hashlib.md5()
        m.update(s)
        result = m.hexdigest()
        return result

if __name__ == '__main__':
    filename = 'testimg.jpeg'
    result = MD5().get_md5(filename)
    print result


