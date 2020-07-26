import numpy as np
import matplotlib.pyplot as plt

kj = 160
# 单位veh/km
uf = 87.84
# 单位 km/h


def draw():
    k1 = np.arange(150)
    u1 = uf*(1 - k1/kj)
    plt.subplot(221)
    plt.plot(k1, u1)
    plt.ylabel("speed")
    plt.xlabel("density")
    plt.title("density-speed")
    plt.subplot(222)
    u2 = np.arange(100)
    q2 = kj * u2 * (1 - u2 / uf)
    plt.plot(q2, u2)
    plt.xlabel("flow")
    plt.ylabel("speed")
    plt.title("flow-speed")
    plt.subplot(223)
    k3 = np.arange(150)
    q3 = k3 * uf * (1 - k3 / kj)
    plt.plot(k3, q3)
    plt.xlabel("density")
    plt.ylabel("flow")
    plt.title("density-flow")
    plt.show()