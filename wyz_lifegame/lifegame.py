# coding=utf-8
import sys, argparse  # argparse是python的一个命令行解析包
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

yeah = ('white', 'black')
cmap = ListedColormap(yeah)

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N,M):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * M, p=[0.2, 0.8]).reshape(N, M) # 采用随机的初始状态

def addGlider(i, j, grid):
    """adds a glider with top-left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])  # 3×3 的 numpy 数组定义了滑翔机图案（看上去是一种在网格中平稳穿越的图案）。
    grid[i:i + 3, j:j + 3] = glider  # 可以看到如何用 numpy 的切片操作，将这种图案数组复制到模拟的二维网格中，它的左上角放在 i和 j指定的坐标，即用这个方法在网格的特定行和列增加一个图案，

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

    # 设置动画模块
    fig, ax = plt.subplots(facecolor='blue')  # 配置 matplotlib 的绘图和动画参数
    img = ax.imshow(grid, cmap=cmap,
                    interpolation='nearest')  # 用plt.show()方法将这个矩阵的值显示为图像，并给 interpolation 选项传入'nearest'值，以得到尖锐的边缘（否则是模糊的）
    ani = animation.FuncAnimation(fig, update,  fargs=(img, grid, N,),frames=10,interval=50,save_count=50)
                                  # animation.FuncAnimation()调用函数 update()，该函数在前面的程序中定义，根据 Conway 生命游戏的规则，采用环形边界条件来更新网格。

    # number of frames?
    # set the output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()

if __name__ == '__main__':
    main()