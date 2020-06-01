#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import numpy as np
import HTMLTestRunner
from test2 import setgridsize

class SetGridTestCace(unittest.TestCase):
    def setUp(self):
        self.number=np.arange(8,101)
        self.clos=self.rows=-1
    def tearDown(self):
        print('test over')
    def test_setgridsize(self):
        self.clos,self.rows=setgridsize()
        print(self.clos,self.rows)
        self.assertIn(self.clos,self.number,'clos out of range')
        self.assertIn(self.rows,self.number, 'rows out of range')
    def test_setgridsize1(self):
        self.clos,self.rows=setgridsize()
        print(self.clos,self.rows)
        self.assertIn(self.clos,self.number,'clos out of range')
        self.assertIn(self.rows,self.number, 'rows out of range')
    def test_setgridsize2(self):
        self.clos,self.rows=setgridsize()
        print(self.clos,self.rows)
        self.assertIn(self.clos,self.number,'clos out of range')
        self.assertIn(self.rows,self.number, 'rows out of range')
    def test_setgridsize3(self):
        self.clos,self.rows=setgridsize()
        print(self.clos,self.rows)
        self.assertIn(self.clos,self.number,'clos out of range')
        self.assertIn(self.rows,self.number, 'rows out of range')
    def test_setgridsize4(self):
        self.clos,self.N=setgridsize()
        print(self.clos,self.rows)
        self.assertIn(self.clos,self.number,'clos out of range')
        self.assertIn(self.rows,self.number, 'rows out of range')
    def test_setgridsize5(self):
        self.clos,self.rows=setgridsize()
        print(self.clos,self.rows)
        self.assertIn(self.clos,self.number,'clos out of range')
        self.assertIn(self.rows,self.number, 'rows out of range')
    def test_setgridsize6(self):
        self.clos,self.rows=setgridsize()
        print(self.clos,self.rows)
        self.assertIn(self.clos,self.number,'clos out of range')
        self.assertIn(self.rows,self.number, 'rows out of range')

if __name__ == '__main__':
    unittest.main()