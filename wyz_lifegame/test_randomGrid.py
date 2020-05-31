#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import matplotlib.pyplot as plt # 生成动画
from test2 import randomGrid

class SetRandGridTestCace(unittest.TestCase):
    def setUp(self):
        self.flag = 'true'
    def tearDown(self):
        print('test over')
    def test_randomGrid(self):
        self.clos=20
        self.rows=30
        self.grid=randomGrid(self.rows,self.clos)
        self.assertEqual(self.grid.size,self.rows*self.clos,msg='不是一个20*30的矩阵')
        for gridvalue in self.grid:
            for value in gridvalue:
                if value!=1 and value!=0:
                    self.flag='false'
                    break
        self.assertEqual(self.flag,'true',msg='细胞生命状态不正确')
    def test_randomGrid1(self):
        self.clos='clos'
        self.rows='rows'
        self.grid=randomGrid(self.rows,self.clos)
        self.assertEqual(self.grid.size,self.rows*self.clos,msg='不是一个矩阵')
    def test_randomGrid2(self):
        self.clos=20
        self.rows=''
        self.grid=randomGrid(self.rows,self.clos)
        self.assertEqual(self.grid.size,self.rows*self.clos,msg='不是一个矩阵')
if __name__ == '__main__':
    unittest.main(verbosity=2)