#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import numpy as np
from test2 import showgrid,randomGrid,update

class ShowgridTestCace(unittest.TestCase):
    def setUp(self):
        self.flag='fail'
        self.grid = randomGrid(20, 30)
    def tearDown(self):
        print('test over')
    def test_showgrid(self):
        self.flag=showgrid(self.grid,20,30)
        self.assertEqual(self.flag,'success', msg='生命游戏运行失败')
    def test_showgrid1(self):
        self.flag=showgrid( 20, 30,self.grid)
        self.assertEqual(self.flag, 'success', msg='生命游戏运行失败')
    def test_showgrid2(self):
        self.flag=showgrid(self.grid,30)
        print("23456")
        self.assertEqual(self.flag, 'success', msg='生命游戏运行失败')

if __name__ == '__main__':
    unittest.main()