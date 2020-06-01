# coding=utf-8
import unittest

class Test_Map(unittest.TestCase):
    # 细胞生命状态测试
    def test_map1(self):
        # 用例
        N = 80
        result = int(N) > 0 and int(N) <= 100
        self.assertEqual(result, True)

    def test_map2(self):
        # 输入边界值
        N=100
        result=int(N) > 0 and int(N) < 101
        self.assertEqual(result,True)

    def test_map3(self):
        # 输入小数
        N=50.1
        result=int(N) > 0 and int(N) < 101
        self.assertEqual(result,True)

    def test_map4(self):
        # 输入负数
        N=-80
        result=int(N) > 0 and int(N) < 101
        self.assertEqual(result,True)

    def test_map5(self):
        # 输入大于100的数
        N=200
        result=int(N) > 0 and int(N) < 101
        self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()
