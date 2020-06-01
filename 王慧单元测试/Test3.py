# coding=utf-8
import unittest
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

class Test_Life(unittest.TestCase):
    # 细胞生命状态测试
    def test_life1(self):
        # 用例1
        grid = 1
        total = 1
        if (total < 2) or (total > 3):
            grid=0
        self.assertEqual(grid, 0)

    def test_life2(self):
        # 用例2
        grid = 1
        total = 4
        if (total < 2) or (total > 3):
            grid=0
        self.assertEqual(grid, 0)

    def test_life3(self):
        # 用例3
        grid = 1
        total = 2
        if (total < 2) or (total > 3):
            grid=0
        self.assertEqual(grid, 1)

    def test_life4(self):
        # 用例4
        grid = 1
        total = 3
        if (total < 2) or (total > 3):
            grid=0
        self.assertEqual(grid, 1)

    def test_life5(self):
        # 用例5
        grid = 0
        total = 3
        if total == 3:
            grid=1
        self.assertEqual(grid, 1)

    def test_life6(self):

        # 用例6
        grid = 0
        total = 2
        if total == 3:
            grid=1
        self.assertEqual(grid, 0)


if __name__ == '__main__':
    unittest.main()
