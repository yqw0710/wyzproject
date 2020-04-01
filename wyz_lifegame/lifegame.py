# coding=utf-8
import sys, argparse  # argparse是python的一个命令行解析包
import numpy as np # 数组
import matplotlib.pyplot as plt # 生成动画
import matplotlib.animation as animation # 更新模拟
from matplotlib.colors import ListedColormap

yeah = ('white', 'black')
cmap = ListedColormap(yeah)

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N,M):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * M, p=[0.2, 0.8]).reshape(N, M) # 采用随机的初始状态

# 实现环形边界条件
def update(frameNum, img, grid, N ,M):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(M):  # 检测网格的8个边缘。用取模运算符让值在边缘折返
            total = int((grid[i, (j - 1) % M] + grid[i, (j + 1) % M] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % M] + grid[(i - 1) % N, (j + 1) % M] +
                         grid[(i + 1) % N, (j - 1) % M] + grid[(i + 1) % N, (j + 1) % M]))
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# 向程序发送命令行参数，mian()
def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--interval', dest='interval', required=False)  # 设置动画更新间隔的毫秒数
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    # 初始化模拟
    # set grid size
    print("请输入一个地图的长与宽：")
    M = input()
    N = input()
    try:
        if M and int(M) > 8:
            M = int(M)
        if N and int(N) > 8:
            N = int(N)
    except ValueError:
        print('The input is not a number!')
        sys.exit(0)

    grid = randomGrid(N)
    # 设置动画模块
    fig, ax = plt.subplots(facecolor='blue')  # 配置 matplotlib 的绘图和动画参数
    img = ax.imshow(grid, cmap=cmap,
                    interpolation='nearest')
    ani = animation.FuncAnimation(fig, update,  fargs=(img, grid, N,),frames=10,interval=50,save_count=50)
    plt.show()

if __name__ == '__main__':
    main()