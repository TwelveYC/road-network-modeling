from time import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn import manifold, datasets
import numpy as np
from tensorly.decomposition import tucker, parafac, non_negative_parafac
from tensorly import kruskal_to_tensor
import tensorly as tl


def t_sne():
    test()


def s_curve():
    n_points = 1000
    X, color = datasets.samples_generator.make_s_curve(n_points)
    n_neighbours = 10
    n_components = 2
    fig = plt.figure(figsize=(8, 8))
    plt.suptitle("Mainfold Learning witi %i points, %i neighbours" %(n_points, n_neighbours), fontsize=14)
    ax = fig.add_subplot(211, projection="3d")
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
    ax.view_init(4, -72)
    t0 = time()
    tsne = manifold.TSNE(n_components=n_components, init="pca", random_state=0)
    Y = tsne.fit_transform(X)
    t1 = time()
    print("划分的时间{}".format(t1-t0))
    # 4.84s
    ax = fig.add_subplot(212)
    plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    plt.show()


def mnist():
    digits = datasets.load_digits(n_class=6)
    data = digits.data
    label = digits.target
    n_samples, n_features = data.shape
    t0 = time()
    tsne = manifold.TSNE(n_components=2, init="pca", random_state=0)
    result = tsne.fit_transform(data)
    t1 = time()
    x_min, x_max = np.min(result, 0), np.max(result, 0)

    print(result.shape)
    print(x_min.shape)
    result = (result - x_min)/(x_max - x_min)
    fig = plt.figure()
    ax = plt.subplot(111)
    print(result)
    for i in range(result.shape[0]):
        plt.text(result[i, 0], result[i, 1], str(label[i]), color=plt.cm.Set1(label[i]/10), fontdict={"weight": "bold", "size": 9})
    print("花费的时间是{}".format(t1-t0))
    plt.show()

    print(n_features)
    print(n_samples)


def test():
    # tl.set_backend('pytorch')
    n = np.loadtxt("data/npy/taxi-speed.txt")
    b = []
    for i in n.T:
        if not (i == 0).all():
            b.append(i)
    b = np.array(b)
    print(b.shape)
    tsne = manifold.TSNE(n_components=2, init="pca", random_state=0)

    result = tsne.fit_transform(b)
    print(result)
    print(result.shape)
    x_min, x_max = np.min(result, 0), np.max(result, 0)

    print(result.shape)
    print(x_min.shape)
    result = (result - x_min)/(x_max - x_min)
    fig = plt.figure()
    ax = plt.subplot(111)
    for i in range(result.shape[0]):
        plt.scatter(result[i, 0], result[i, 1])
    plt.show()




