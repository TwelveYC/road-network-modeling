import xlrd
import networkx as nx
import os
import numpy as np
import sys
import json
from coordTransform_py.coordTransform_utils import wgs84_to_gcj02
from functools import reduce


def process_data():
    get_visual_data()


def preprocess_data():
    """
    数据预处理，从表格到初级的网络数据
    :return:
    """
    g = nx.read_graphml("net.graphml")
    edge_attr = {}
    edge_table = xlrd.open_workbook("data/UTN/Shapefiles/roadNetwork/edges/edges.xlsx").sheet_by_index(0)
    # 边的字段有：from highway length oneway to nodescount road_id
    for i in range(1, edge_table.nrows):
        v = edge_table.row(i)
        index = tuple([v[0].value, v[4].value, 0])
        if index in edge_attr.keys():
            index = tuple([v[0].value, v[4].value, 1])
        edge_attr.update({
            index: {
                "highway": v[1].value,
                "length": v[2].value,
                "oneway": v[3].value,
                "NodesCount": v[5].value,
                "roadid": v[6].value
            }
        })
    nx.set_edge_attributes(g, edge_attr)


def correct_data():
    """
    矫正数据当中的错误
    :return:
    """
    a = nx.Graph()
    a.number_of_edges()
    g = nx.read_graphml("net.graphml")
    h = nx.read_graphml("data/changchun.graphml")
    print(g.number_of_edges())
    edge_attr = {}
    for i in g.edges:
        if i in h.edges:
            c = h.edges[i].copy()
            print(c)
            c.pop("length")
            c.pop("oneway")
            c.pop("highway")
            edge_attr.update({
                i: c
            })
    nx.set_edge_attributes(g, edge_attr)
    nx.write_graphml(g, "net1.graphml")


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


def get_visual_data():
    """
    处理获得可视化的json数据
    :return:
    """
    g = nx.read_graphml("net.graphml")
    nodes = g.nodes
    edges = g.edges
    data = {}
    links = list()
    vertex = list()

