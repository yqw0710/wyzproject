# coding=utf-8
import unittest
import numpy as np


class Test_Init(unittest.TestCase):
    #初始二维数组测试
    def test_init1(self):
        # 输入小于101and 大于0的整数
        N=80
        result = np.zeros(N * N).reshape(N, N)
        self.assertEqual(result, "null")

    def test_init2(self):
        # 输入边界值
        N = 100
        result = np.zeros(N * N).reshape(N, N)
        self.assertEqual(result, "null")

    def test_init3(self):
        # 输入小数
        N = 50.1
        result = np.zeros(N * N).reshape(N, N)
        self.assertEqual(result, "null")

    def test_init4(self):
        # 输入负数
        N = -80
        result = np.zeros(N * N).reshape(N, N)
        self.assertEqual(result,"null")

    def test_init5(self):
        # 输入大于100的数
        N = 200
        result = np.zeros(N * N).reshape(N, N)
        self.assertEqual(result, "null")

if __name__ == '__main__':
    unittest.main()
