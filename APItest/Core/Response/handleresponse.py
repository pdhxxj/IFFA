#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author='Jingle,RRJC.CO.LTD'
import json
from Utils.Json import Json
from Utils.Xml import Xml
from Utils.Js import Js
from Utils.Jar import HandleJar


class HANDLERESPONSE(object):

    def __init__(self):
        pass

    def judge_typedata(self, res):
        content_type = res['req_headers']['Content-Type']
        return content_type

    def handle_json(self, res):
        res_json = json.loads(res['req_content'])
        # 留个口后续可能会详细处理json
        Json.HANDLEJSON().parsejson()
        return res_json

    def handle_xml(self, res):
        res_xml = res['req_content']
        # 留个口后续可能会详细处理xml
        Xml.HANDLEXML().parsexml()
        return res_xml

    def handle_js(self, res):
        res_js = res['req_content']
        #留个口后续可能会详细处理js
        Js.HANDLEJS().parsejs()
        return res_js

    def handle_other(self, res):
        res_other = res['req_content']
        return res_other

    def handle_httpres(self, res):
        content_type = self.judge_typedata(res)
        if 'application/json' in content_type.lower():
            res_data = self.handle_json(res)
            return res_data
        elif 'text/html' in content_type.lower():
            res_data = self.handle_html(res)
            return res_data
        elif 'text/xml' in content_type.lower() or 'application/xml' in content_type.lower():
            res_data = self.handle_xml(res)
            return res_data
        elif 'script' in content_type.lower():
            res_data = self.handle_js(res)
            return res_data
        else:
            res_data = self.handle_other(res)
            return res_data

    def handle_resentity(self, entity, res):
        HandleJar.HandleJar().entity2dict(jarname, entity,classname, res)
        return '', ''

