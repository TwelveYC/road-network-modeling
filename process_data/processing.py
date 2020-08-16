import xlrd
import networkx as nx
import os
import numpy as np
import sys
import json
from coordTransform_py.coordTransform_utils import wgs84_to_gcj02
from functools import reduce


def process_data():
    process_tensor()


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


    # speeds = np.empty([7, 24, 21101])
    # volumes = np.empty([7, 24, 21101])
    # print("ok")
    # print("ok")
    # # for i in range(5, 12):
    # #     path = taxi_volume.format(get_char_index(i))
    # #     t = get_tensor(path)
    # #     print(t[:,5])
    # edge_table = xlrd.open_workbook("data/UTN/Shapefiles/roadNetwork/edges/edges.xlsx").sheet_by_index(0)
    # # # 边的字段有：from highway length oneway to nodescount road_id
    # for i in range(5, 12):
    #     path = bus_volume.format(get_char_index(i))
    #     volumes[i-5, :, :] = get_tensor(path)
    #
    # v = edge_table.col(2)
    # r = np.empty([7, 24, 21101])
    # index = 0
    # for i in v:
    #     if i.value != "length":
    #         r[:, :, index] = np.true_divide(volumes[:, :, index], float(i.value)/1000)
    #         index += 1
    # np.save("bus-flow", r)
    # np.save("bus-volume", volumes)






def get_visual_json_data():
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

    def get_geometry(n):
        temp = list()
        for i in n[12:-1].split(","):
            i = i.strip().split(" ")
            temp.append(wgs84_to_gcj02(float(i[0]), float(i[1])))
        return temp

    for node in nodes:
        current_node = nodes[node]
        if current_node.get("lon"):
            coordinate = wgs84_to_gcj02(float(current_node.get("lon")), float(current_node.get("lat")))
            vertex.append({
                "id": node,
                "lon": coordinate[0],
                "lat": coordinate[1],
            })
        else:
            vertex.append({
                "id": node,
                "lon": None,
                "lat": None,
            })
    for edge in edges:
        current_edge = edges[edge]
        if current_edge.get("geometry"):
            geometry = get_geometry(current_edge.get("geometry"))
            source = nodes[edge[0]]
            target = nodes[edge[1]]
            geometry.insert(0, wgs84_to_gcj02(float(source.get("lon")), float(source.get("lat"))))
            geometry.append(wgs84_to_gcj02(float(target.get("lon")), float(target.get("lat"))))
            links.append({
                "id": edge,
                "source": edge[0],
                "target": edge[1],
                "geometry": geometry,
                "length": current_edge.get("length"),
            })
        else:
            links.append({
                "id": edge,
                "source": edge[0],
                "target": edge[1],
                "geometry": None,
                "length": current_edge.get("length"),
            })

    data["node"] = vertex
    data["edge"] = links

    with open("changchun2.json", "w") as fp:
        json.dump(data, fp)

