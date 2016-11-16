#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import sys


class Txt(object):

    def __init__(self):
        pass

    def input_casetxt(self, filename, para):
        with open(filename, 'w')as f:
            sys.stdout = f
            print '{'
            i = 1
            for k in para:
                if i < len(para):
                    print "'%s': '%s', "%(k, para[k])
                else:
                    print "'%s': '%s'"%(k, para[k])
                i += 1
            print '}'

if __name__ == '__main__':
    para = {'value1': u'\u6211\u59d3\u53e4',
            'value2': 'abcdefg',
            'tag': 1,
            'user': 'maas'
            }
    filename = 'C:/api_test/testxt.txt'
    Txt().input_casetxt(filename, para)
