#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'

import os
from Common.Exception import HandleException


class FILE(object):
    def __init__(self):
        pass

    def write_bfile(self, filename, write):
        try:
            if os.path.exists(filename):
                with open(filename, 'a+')as f:
                    f.write(write)
            else:
                with open(filename, 'wb')as f:
                    f.write(write)
        except:
            HandleException.Exception().systemerror('write %s is Error !' % filename)

    def read_bfile(self, filename):
        try:
            with open(filename, 'rb')as f:
                result = f.read()
            return result
        except:
            HandleException.Exception().systemerror('read %s is Error !' % filename)

    def write_file(self, filename, write):
        try:
            if os.path.exists(filename):
                with open(filename, 'a+') as f:
                    f.write(write)
            else:
                with open(filename, 'w') as f:
                    f.write(write)
        except:
            HandleException.Exception().systemerror('write %s is Error !' % filename)

    def read_file(self, filename):
        try:
            with open(filename, 'r')as f:
                result = f.read()
            return result
        except:
            HandleException.Exception().systemerror('read %s is Error !' % filename)

    def get_size(self, filename):
        size = os.path.getsize(filename)
        return size

    def make_dir(self, dirname):
        if os.path.exists(dirname) == False:
            os.mkdir(dirname)
        else:
            HandleException.Exception().systemerror('%s is exist! can not build %s' % dirname)

    def all_files(self, root):
        flist = []
        for path, subdirs, files in os.walk(root):
            for f in files:
                flist.append(os.path.join(path, f))
        return flist

if __name__ == '__main__':
    r = FILE().make_dir('test')
    print r

