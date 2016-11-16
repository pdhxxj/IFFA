#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import json
import decimal

# 调试数据
jdata = {'name': 'Jingle',
         'work': {'pingan': 'PingAn',
                  'liao': 'liao',
                  'RRJC': ['RRJC', '1234', 989]
                  },
         'age': 25,
         'friend': ['Yan', 'Lu']
         }


# 解析第一层的json数据
class HANDLEJSON(object):
    def __init__(self):
        pass


    def get_1json(self, jndata):
        outjson = {}
        for k in jndata:
            outjson[k] = jndata[k]
            print '  ', k, ':', outjson[k]
        return outjson

    # 解析第二层及以上的json数据
    def get_2json(self, jndata):
        outjson = {}
        for k in jndata:
            outjson[k] = jndata[k]
            print '    ', k, ':', outjson[k]
        return outjson

    # 解析第一层的list数据
    def get_list(self, jndata):
        outlist = []
        for i in range(len(jndata)):
            outlist.append(jndata[i])
            print '  ', i, ':', jndata[i]
        return outlist

    # 获取第二层及以上的list数据
    def get_2list(self, jndata):
        outlist = []
        for i in range(len(jndata)):
            outlist.append(jndata[i])
            print '    ', i, ':', jndata[i]
        return outlist

    # 解析json数据方法
    def get_3json(self, jdata):
        outjson = {}
        for k in jdata:
            out2json = {}
            if isinstance(jdata[k], dict):
                print k, ':'
                outjson[k] = self.get_1json(jdata[k])
                for k2 in outjson[k]:
                    if isinstance(outjson[k][k2], dict):
                        print '  ', k2, ':'
                        out2json[k2] = self.get_2json(outjson[k][k2])
                    elif isinstance(outjson[k][k2], list):
                        print '  ', k2, ':'
                        out2json[k2] = self.get_2list(outjson[k][k2])

            elif isinstance(jdata[k], list):
                print k, ':'
                outjson[k] = self.get_list(jdata[k])

            else:
                outjson[k] = jdata[k]
                print k, ':', outjson[k]
        print 'Whole Json Data:', outjson
        return outjson

    def parsejson(self):
        pass


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, dict):
            return obj.isoformat()
        else:
            return super(CustomJSONEncoder, self).default(obj)

if __name__ == '__main__':
    a = json.dumps(jdata, cls=CustomJSONEncoder, ensure_ascii=False)
    print a

