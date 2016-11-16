#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

import itertools
from Common.Exception import HandleException


class ITER(object):

    def __index__(self):
        pass

    # 生成排列组合
    def iter_data(self, paralist):
        list2 = []

        for i in range(1,len(paralist)+1):
            iter = itertools.combinations(paralist, i)
            list2.append(list(iter))

        return list2

    # 单种情况case的inputdata输出
    def combinate_data(self, single, paradata):
        in_paradata = {}
        for i in range(len(single)):
            in_paradata[single[i]] = paradata[single[i]]
        return in_paradata

    def lackpara(self, paramslist, ruler_data):
        try:
            paralist = {}
            # 先拼一种全值情况
            for k in paramslist:
                paralist[k] = paramslist[k][0]['value']
            for k in paralist:
                # 从ruler中判定必填项，删除遇到的第一个必填项
                if ruler_data[k]['notnull'] == True:
                    del paralist[k]
                    break
                else:
                    continue
            return paralist
        except Exception,e:
            HandleException.Exception().exception('lackpara raise exception:\n' + e)

    def allpairs(self, paramslist):
        try:
            parameters_map = {}
            parameters = []
            i = 0
            for k in paramslist:
                parameters_map[str(i)] = k
                parameters.append(paramslist[k])
                i += 1
            pairwise = all_pairs(parameters)
            out = []
            for i2,v in enumerate(pairwise):
                singleout = {}
                for i3 in range(len(v)):
                    singleout[parameters_map[str(i3)]] = v[i3]
                out.append(singleout)

            for i4 in range(len(out)):
                single_para = out[i4]
                false = 0
                for k2 in single_para:
                    if single_para[k2]['except'] == False:
                        single_para[k2] = single_para[k2]['value']
                    else:
                        single_para[k2] = single_para[k2]['value']
                        false += 1
                if false == 0:
                    single_para['error'] = False
                else:
                    single_para['error'] = True
            return out
        except Exception,e:
            HandleException.Exception().exception('allpairs raise exception:\n' + e)

if __name__ == '__main__':
    paralist = {'user': ['gujin', 'yanxiaoli', 'daben', 'nima', 'ow'],
                'password': ['133', '123', '321', '666'],
                'theme' : ['haha', 'hehe', 'niyaya', 'guda'],
                'wo': ['yu', 'we', 'ti', 'wo']
                }
    result = ITER().lackpara(paralist)
    print len(result),result

