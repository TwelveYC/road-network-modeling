import xlrd
import networkx as nx
import json
import os
import numpy as np
import sys


def process_data():
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


#  矫正原始数据当中的问题
def correct_data():
    g = nx.read_graphml("net1.graphml")
    h = nx.read_graphml("加入边经纬度之后的数据.graphml")
    a = nx.Graph()
    index = 0
    h_nodes = h.nodes
    node_attr = {}
    for i in g.nodes:
        if len(h_nodes[i]) is not 0:
            node_attr.update({
                i: {
                    "lon": h_nodes[i].get("lon"),
                    "lat": h_nodes[i].get("lat"),
                }
            })
            index += 1
    print(index)
    nx.set_node_attributes(g, node_attr)
    nx.write_graphml(g, "net2.gml")


def get_all_tensor():
    taxi_speed = "data/UTN/Taxi-utn/Taxi-utn-speed"
    taxi_volume = "data/UTN/Taxi-utn/Taxi-utn-volume"
    bus_speed = "data/UTN/Bus-utn/Bus-utn-speed"
    bus_volume = "data/UTN/Bus-utn/Bus-utn-volume"
    paths = os.listdir(taxi_speed)
    speeds = np.empty([7, 24, 21101])
    volumes = np.empty([7, 24, 21101])
    print(paths[0])
    get_tensor(taxi_speed + "/" + paths[0])


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
    # for i in range(21101):
    #     print(n[:, i])
    # for i in range(10):
    #     print(n[:, i])
    print(n[:, -1])

