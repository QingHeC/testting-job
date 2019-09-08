#!/usr/bin/env python
#coding:utf-8

from .interface_http import interface_http
# coding:utf-8
import unittest
from auto_interface.api_auto.configs.config import basedir
from auto_interface.api_auto.lib import HTMLTestRunner
import time

class central_control():

    def __init__(self):

        pass



    def control_inter_http(self,):
        print("1111111")
        #执行用例的位置


        interf_html = interface_http().req_requests("get","http://www.baidu.com")
        return interf_html

    def control_inter_webserver(self):

        pass

    def control_web_Ui(self):
        pass


if __name__ == "__main__":
    central_control().control_inter_http()