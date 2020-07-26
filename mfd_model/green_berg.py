import numpy as np
import matplotlib.pyplot as plt

km = 59.26
# 阻塞密度
um = 28.56
# 最佳速度

def draw():
    # 1 横坐表是流量，纵坐标是速度
    # 2 横坐标是密度，纵坐标是速度
    # 3 横坐标是密度，纵坐标是流量
    u1 = np.arange(100)
    q1 = km * u1 * np.exp(-u1/um)
    plt.subplot(221)
    plt.plot(q1, u1)
    plt.xlabel("flow")
    plt.ylabel("speed")
    plt.title("flow-speed")
    plt.subplot(222)
    k2 = np.arange(120)
    u2 = um * np.log(km/k2)
    plt.plot(k2, u2)
    plt.xlabel("density")
    plt.ylabel("speed")
    plt.title("density-speed")
    plt.subplot(223)
    k3 = np.arange(60)
    q3 = k3 * um * np.log(km / k3)
    plt.plot(k3, q3)
    plt.xlabel("density")
    plt.ylabel("flow")
    plt.title("density-flow")
    plt.show()
