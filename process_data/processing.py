import xlrd
import networkx as nx
import os
import numpy as np
import sys
import json
from coordTransform_py.coordTransform_utils import wgs84_to_gcj02
from functools import reduce
import matplotlib.pyplot as plt


def process_data():
    correct_data()


def preprocess_data():
    """
    数据预处理，从表格到初级的网络数据
    :return:
    """
    g = nx.Graph()
    edge_attr = {}
    node_attr = {}
    node_table = xlrd.open_workbook("data/UTN/Shapefiles/roadNetwork/nodes/nodes.xlsx").sheet_by_index(0)
    edge_table = xlrd.open_workbook("data/UTN/Shapefiles/roadNetwork/edges/edges.xlsx").sheet_by_index(0)
    nodes = list()
    edges = list()
    for i in range(1, node_table.nrows):
        v = node_table.row(i)
        nodes.append(v[2].value)
        node_attr.update({
            v[2].value: {
                "lat": v[0].value,
                "lon": v[1].value,
            }
        })

    # 边的字段有：from highway length oneway to nodes count road_id
    for i in range(1, edge_table.nrows):
        v = edge_table.row(i)
        u = tuple([v[0].value, v[4].value])
        uT = tuple([v[4].value, v[0].value])
        if u not in edges and uT not in edges:
            edges.append(u)
            edge_attr.update({
                u: {
                    "highway": v[1].value,
                    "length": [v[2].value],
                    "oneway": v[3].value,
                    "roadid": [v[6].value]
                }
            })
        else:
            if u not in edges:
                u = uT
            edge_attr[u]["length"].append(v[2].value)
            edge_attr[u]["roadid"].append(v[6].value)

    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    nx.set_node_attributes(g, node_attr)
    nx.set_edge_attributes(g, edge_attr)
    nx.write_gpickle(g, "net.gpickle")


def correct_data():
    """
    矫正数据当中的错误
    :return:
    """
    g = nx.read_gpickle("net.gpickle")
    edges = []
    with open("data/出租车网络边有数据的边id.json", "r") as fp:
        edges_id = json.load(fp)
    print(edges_id)
    print(len(edges_id))
    g_edges = g.edges
    for i in g_edges:
        v = g_edges[i]
        ids = v.get("roadid")
        is_all = True
        for id in ids:
            if id not in edges_id:
                is_all = False
                break
        if is_all:
            edges.append(i)
    print(edges)
    print(len(edges))
    h = g.edge_subgraph(edges).copy()
    nx.write_gpickle(h, "taxi-net.gpickle")
    print(h.number_of_edges())
    print(h.number_of_nodes())







def process_tensor():
    """
    张量处理相关函数
    :return:
    """
    taxi_speed = "data/UTN/Taxi-utn/Taxi-utn-speed/Day-201803{}-taxi-speed.txt"
    taxi_volume = "data/UTN/Taxi-utn/Taxi-utn-volume/Day-201803{}-taxi-volume.txt"
    bus_speed = "data/UTN/Bus-utn/Bus-utn-speed/Day-201803{}-bus-speed.txt"
    bus_volume = "data/UTN/Bus-utn/Bus-utn-volume/Day-201803{}-bus-volume.txt"

    def get_tensor(path):
        np.set_printoptions(threshold=sys.maxsize)
        n = np.empty([24, 21101])
        # 21101 条边
        with open(path, "r") as fp:
            lines = fp.read().splitlines()
            for line in lines:
                l = line.split(",")
                a = [float(i) for i in l][1:]
                n[:, int(l[0])] = a
        return n

    def get_char_index(n):
        return "".join(["00", str(n)])[-2:]
    speeds = np.empty([168, 21101])
    for i in range(5, 12):
        path = bus_volume.format(get_char_index(i))
        speeds[(i- 1 - 4) * 24: (i - 4) * 24, :] = get_tensor(path)
        print(path)
    np.savetxt('bus-volume.txt', speeds, fmt='%.2f')


