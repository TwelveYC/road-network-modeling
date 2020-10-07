from process_data.processing import process_data
from process_data.process_sumo_data import get_sumo_data
from dimensionality_reduce.t_sne import t_sne
from simulations import artifical_network
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import json
import random
from queue import PriorityQueue
from utils.dijkstra import dijkstra_edge_min_heap


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
    if step_func == "process_data":
        get_sumo_data()
    elif step_func == "analysis_network":
        g = nx.read_gpickle("data/gpickle/bus-net.gpickle")
        h = nx.read_gpickle("data/gpickle/net.gpickle")
        nodes = g.nodes
        h_nodes = h.nodes
        for node in nodes:
            if node not in h_nodes:
                print("ok")
                print(node)
    elif step_func == "mfd_model_analysis":
        pass
    elif step_func == "dimensionality_reduction":
        t_sne()
    elif step_func == "artificial_network_simulation":
        artifical_network.emulation()
    elif step_func == "test_module":
        print("ok")





if __name__ == '__main__':
    main()
