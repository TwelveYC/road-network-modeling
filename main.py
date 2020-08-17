from process_data.processing import process_data
from tensorly.decomposition import tucker, parafac, non_negative_parafac
from tensorly import kruskal_to_tensor
import tensorly as tl
import numpy as np
from time import time
from mfd_model import green_shields, green_berg, under_wood
from dimensionality_reduce.t_sne import t_sne
import networkx as nx
import json
step = 1

step_dict = {
    1: "process_data",
    2: "analysis_network",
    3: "mfd_model_analysis",
    4: "dimensionality_reduction",
}


def main():
    step_func = step_dict.get(step)
    if step_func is "process_data":
        process_data()
    elif step_func is "analysis_network":
        n = np.mat(np.random.random([3, 8]))
        print(n)
        u,s,v = np.linalg.svd(n, full_matrices=False)
        print(u.shape)
        print(s.shape)
        print(v.shape)
        print(np.dot(u, np.dot(np.diag(s), v)))
        # speeds = np.loadtxt("data/npy/taxi-speed.txt")
        # volumes = np.loadtxt("data/npy/taxi-flow.txt")
        # print(np.max(volumes))
        # print(np.argmax(volumes))
        # data = []
        # for i in range(21001):
        #     temp = []
        #     s = speeds[:, i]
        #     v = volumes[:, i]
        #     for j in range(168):
        #         temp.append([s[j], v[j]])
        #     data.append(temp)
        # with open("taxi-flow.json", "w") as fp:
        #     json.dump(data, fp)
        # g = nx.read_graphml("net.graphml")
        # edges = g.edges
        # flow = np.zeros([168, 21101])
        # for index in edges:
        #     edge = edges[index]
        #     id = int(edge.get("roadid"))
        #     length = float(edge.get("length"))
        #     v = volumes[:, id]
        #     flow[:, id] = v/(length/1000)
        # np.savetxt("taxi-flow.txt", flow, fmt="%.4f")



        # 横坐标是速度，纵坐标是流量

    elif step_func is "mfd_model_analysis":
        under_wood.draw()
    elif step_func is "dimensionality_reduction":
        t_sne()


if __name__ == '__main__':
    main()
