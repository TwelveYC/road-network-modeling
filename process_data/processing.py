import json
import time
import xlrd
import networkx as nx
import igraph as ig


def process_data():
    g = nx.Graph()
    node_table = xlrd.open_workbook("data/UTN/Shapefiles/roadNetwork/nodes/nodes.xlsx").sheet_by_index(0)
    nodes = []
    edges = []
    node_attr = {}
    edge_attr = {}
    # lat lon osmid
    # {"节点id":{key1:value1}}
    for i in range(node_table.nrows):
        v = node_table.row(i)
        if v[2].value != "osmid":
            nodes.append(v[2].value)
            node_attr.update({
                v[2].value: {
                    "lat": v[0].value,
                    "lon": v[1].value,
                }
            })
    edge_table = xlrd.open_workbook("data/UTN/Shapefiles/roadNetwork/edges/edges.xlsx").sheet_by_index(0)
    # from highway length oneway to nodescount road_id
    for i in range(edge_table.nrows):
        v = edge_table.row(i)
        if v[0].value != "from":
            k = tuple([v[0].value, v[4].value])
            edges.append(k)
            edge_attr.update({
                k: {
                    "highway": v[1].value,
                    "length": v[2].value,
                    "oneway": v[3].value,
                    "NodesCount": v[5].value,
                    "roadid": v[6].value
                }
            })
    print(nodes)
    print(node_attr)
    # g.add_nodes_from(nodes)
    # g.add_edges_from(edges)
    # nx.set_node_attributes(g, node_attr)
    # nx.set_edge_attributes(g, edge_attr)
    # nx.write_gml(g, "net.gml")