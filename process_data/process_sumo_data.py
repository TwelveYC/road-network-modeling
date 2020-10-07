import networkx as nx
import matplotlib.pyplot as plt
from xml.dom import minidom


def get_sumo_data():
    g = nx.grid_2d_graph(6, 6)
    dom = minidom.Document()
    nodes = dom.createElement("nodes")
    nodes.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    nodes.setAttribute("xsi:noNamespaceSchemaLocation", "http://sumo.dlr.de/xsd/nodes_file.xsd")
    vs = g.nodes
    index = 0

    def get_index(i):
        return str(6*i[0]+i[1])
    for i in vs:
        node = dom.createElement("node")
        node.setAttribute("id", str(index))
        node.setAttribute("x", str(i[0]*250))
        node.setAttribute("y", str(i[1]*250))
        nodes.appendChild(node)
        index += 1

    dom.appendChild(nodes)
    with open("sumo.nod.xml", "w") as fp:
        dom.writexml(fp, indent="\t", newl="\n", encoding="utf-8")

