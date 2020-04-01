# coding=utf-8
import sys, argparse  # argparse是python的一个命令行解析包
import numpy as np # 数组
import matplotlib.pyplot as plt # 生成动画
import matplotlib.animation as animation # 更新模拟
from matplotlib.colors import ListedColormap

yeah = ('LightPink', 'black')
cmap = ListedColormap(yeah)

ON = 1
OFF = 0
vals = [ON, OFF]

# 初始化细胞生命状态
def randomGrid(N):# returns a grid of NxN random values
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)

#更新细胞生命状态
def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):# 检测网格的8个边缘。用取模运算符让值在边缘折返
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]))
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

def main():
    # set grid size
    print("请输入一个地图的大小值：")
    N = input()
    try:
        if N and int(N) > 8:
            N = int(N)
    except ValueError:
        print('The input is not a number!')
        sys.exit(0)

    # declare grid
    grid = randomGrid(N)

    parser = argparse.ArgumentParser()
    parser.add_argument('--interval', dest='interval', required=False) # 设置动画更新间隔的毫秒数
    args = parser.parse_args()
    # 设置动画
    fig, ax = plt.subplots(facecolor='Lavender')  # 配置 matplotlib 的绘图和动画参数
    img = ax.imshow(grid, cmap=cmap,interpolation='nearest')  # 用plt.show()方法将这个矩阵的值显示为图像，并给 interpolation 选项传入'nearest'值，以得到尖锐的边缘（否则是模糊的）
    ani =animation.FuncAnimation(fig, update, fargs=(img, grid, N,),frames=10,interval=50,save_count=50)
             # animation.FuncAnimation()调用函数 update()，该函数在前面的程序中定义，根据命游戏的规则更新网格。
    plt.show()

# 只有在文件作为脚本直接执行时才会被执行，而 import 到其他脚本中是不会被执行的。
if __name__ == '__main__':
    main()