from process_data.processing import process_data
from dimensionality_reduce.t_sne import t_sne
from simulations import artifical_network
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import json
import random
from queue import PriorityQueue
from utils.dijkstra import dijkstra
from utils.min_heap import MinHeap
step = 6

step_dict = {
    1: "process_data",
    2: "analysis_network",
    3: "mfd_model_analysis",
    4: "dimensionality_reduction",
    5: "artificial_network_simulation",
    6: "test_module"
}


def main():
    step_func = step_dict.get(step)
    # nx.shortest_path()
    if step_func is "process_data":
        process_data()
    elif step_func is "analysis_network":
        g = nx.read_gpickle("data/gpickle/bus-net.gpickle")
        h = nx.read_gpickle("data/gpickle/net.gpickle")
        nodes = g.nodes
        h_nodes = h.nodes
        for node in nodes:
            if node not in h_nodes:
                print("ok")
                print(node)
    elif step_func is "mfd_model_analysis":
        pass
    elif step_func is "dimensionality_reduction":
        t_sne()
    elif step_func is "artificial_network_simulation":
        artifical_network.emulation()
    elif step_func is "test_module":
        g = nx.read_gml("test.gml")
        dijkstra(g, "0")



if __name__ == '__main__':
    main()
