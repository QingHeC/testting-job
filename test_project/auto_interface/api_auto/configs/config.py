#!/usr/bin/env python
#coding:utf-8

import os

#数据目录
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')

#项目目录
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 运行任务的列表
run_lis = []

#附件保存位置
file_save_path = "save_files"

print(basedir)

#日志配置
import logging
logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'logs')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt = '%y-%m-%d %H:%M',
                    filename=os.path.join(logpath,'log.txt'),
                    filemode='a'
                    )

