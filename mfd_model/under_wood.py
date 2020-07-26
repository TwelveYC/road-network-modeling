import numpy as np
import matplotlib.pyplot as plt
km = 51.88
uf = 32.54

def draw():
    u1 = np.arange(80)
    q1 = km * u1 * np.log(uf / u1)
    plt.subplot(221)
    plt.plot(q1, u1)
    plt.xlabel("flow")
    plt.ylabel("speed")
    plt.title("flow-speed")

    plt.subplot(222)
    k2 = np.arange(100)
    u2 = uf * np.exp(-k2/km)
    plt.plot(k2, u2)
    plt.xlabel("density")
    plt.ylabel("speed")
    plt.title("density-speed")


    plt.subplot(223)
    k3 = np.arange(100)
    q3 = k3 * uf * np.exp(-k3 / km)
    plt.plot(k3, q3)
    plt.xlabel("density")
    plt.ylabel("flow")
    plt.title("density-flow")

    plt.show()
