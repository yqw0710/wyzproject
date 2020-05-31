#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import matplotlib.pyplot as plt # 生成动画
from matplotlib.colors import ListedColormap
from test2 import update,randomGrid

class SetUpdateTestCace(unittest.TestCase):
    def setUp(self):
        self.grid= randomGrid(9, 9)
        self.grid1=self.grid.copy()
        self.yeah = ('LightPink', 'black')
        self.cmap = ListedColormap(self.yeah)
        self.fig, self.ax = plt.subplots(facecolor='Lavender')  # 配置 matplotlib 的绘图和动画参数
        self.img = self.ax.imshow(self.grid, cmap=self.cmap, interpolation='nearest')
    def tearDown(self):
        print('test over')
    def test_update(self):
        self.img=update(10, self.img, self.grid,9,9)
        for x,y in zip(self.grid,self.grid1):
            for i,j in zip(x,y):
                if i!=j:
                    self.flag='true'
                    break
        print(self.grid1)
        print(self.grid)
        self.assertEqual(self.flag,'false', msg='地图没有更新')
    def test_update1(self):
        self.img=update(9,9,10, self.img, self.grid)
        for x,y in zip(self.grid,self.grid1):
            for i,j in zip(x,y):
                if i!=j:
                    i=2
                    break
        self.assertEqual(i,2, msg='地图没有更新')
    def test_update2(self):
        self.img=update(10, self.img, self.grid)
        for x,y in zip(self.grid,self.grid1):
            for i,j in zip(x,y):
                if i!=j:
                    i=2
                    break
        self.assertEqual(i,2, msg='地图没有更新')

if __name__ == '__main__':
    unittest.main(verbosity=2)