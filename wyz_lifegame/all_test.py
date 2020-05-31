#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import HTMLTestRunner
import unittest
import os,time

listaa = "E:\\study\\软件工程\\实验\结对编程\\wyzproject\\wyz_lifegame"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="E:\\study\\软件工程\\实验\结对编程\\wyzproject\\wyz_lifegame\\"+now+"_result.html"
fp=open(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'生命游戏测试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()