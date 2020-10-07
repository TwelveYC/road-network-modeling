import networkx as nx
from matplotlib import pyplot as plt
from queue import PriorityQueue

inf = 1e12


class Element:
    def __init__(self, node, value, last_point):
        self.node = node
        self.value = value
        self.last_point = last_point

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def dijkstra_heap_node_min(g, source):
    inf = 1e12
    dis_node = nx.get_node_attributes(g, "dis")
    n = g.number_of_nodes()
    v = [0 for i in range(n)]
    dis = [inf for i in range(n)]
    paths = ["-1" for i in range(n)]
    for i in nx.neighbors(g, source):
        dis[int(i)] = dis_node[str(i)]
    pq = PriorityQueue()
    pq.put(Element(source, -1, "0"))
    while not pq.empty():
        k = pq.get()
        index = int(k.node)
        if v[index]:
            continue
        v[index] = 1
        dis[index] = k.value
        paths[index] = k.last_point
        for i in nx.neighbors(g, k.node):
            pq.put(Element(i, k.value + dis_node.get(i), k.node))
    return paths, dis


# ['-1', '16', '12', '1', '17', '12', '2', '19', '15', '7', '-1', '13', '17', '-1', '13', '-1', '10', '11', '12', '-1']
# [1000000000000.0, 15, 17, 21, 17, 23, 20, 11, 15, 14, 8, 5, 14, 3, 9, 9, 9, 11, 21, 5]


def dijkstra_node(g, source):
    dis_node = nx.get_node_attributes(g, "dis")
    n = g.number_of_nodes()
    v = [0 for i in range(n)]
    int_source = int(source)
    dis = [inf for i in range(n)]
    paths = ["0" for i in range(n)]
    v[int_source] = 1
    for i in nx.neighbors(g, source):
        dis[int(i)] = dis_node[str(i)]
    for i in range(n):
        k = 0
        for j in range(n):
            if not v[j] and (k is 0 or dis[j] < dis[k]):
                k = j
        v[k] = 1
        for j in nx.neighbors(g, str(k)):
            index = int(j)
            if not v[index] and dis[k] + dis_node.get(j) < dis[index]:
                dis[index] = dis[k] + dis_node.get(j)
                paths[index] = str(k)
    return paths, dis


def get_edge_index(a, b, dis):
    try:
        value = dis[(a, b)]
    except KeyError:
        value = dis[(b, a)]
    return value

class NodeElement:
    def __init__(self, node, value, last_point):
        self.node = node
        self.value = value
        self.last_point = last_point

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def dijkstra_edge_min_heap(g, source):
    dis_edge = nx.get_edge_attributes(g, "dis")
    n = g.number_of_nodes()
    v = [0 for i in range(n)]
    dis = [inf for i in range(n)]
    paths = ["-1" for i in range(n)]
    for i in nx.neighbors(g, source):
        dis[int(i)] = get_edge_index(source, i, dis_edge)
    pq = PriorityQueue()
    pq.put(NodeElement(source, -1, source))
    while not pq.empty():
        k = pq.get()
        index = int(k.node)
        if v[index]:
            continue
        v[index] = 1
        dis[index] = k.value
        paths[index] = k.last_point
        for i in nx.neighbors(g, k.node):
            pq.put(NodeElement(i, k.value + get_edge_index(k.node, i, dis_edge), k.node))
    print(paths)
    print(dis)



