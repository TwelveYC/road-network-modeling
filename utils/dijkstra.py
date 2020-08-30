import networkx as nx
from matplotlib import pyplot as plt
from queue import PriorityQueue


class Element:
    def __init__(self, node, value):
        self.node = node
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def dijkstra(g, source):
    inf = 1e12
    dis_node = nx.get_node_attributes(g, "dis")
    n = g.number_of_nodes()
    v = [0 for i in range(n)]
    int_source = int(source)
    dis = [inf for i in range(n)]
    paths = ["-1" for i in range(n)]
    v[int_source] = 1
    for i in nx.neighbors(g, source):
        dis[int(i)] = dis_node[str(i)]
    pq = PriorityQueue()
    pq.put(Element("1", 0))
    pq.put(Element("2", 5))
    pq.put(Element("4", 6))
    pq.put(Element("5", 9))
    print(type(pq.get()))
    print(pq.get().value)
    print(pq.get().value)
    return paths, dis
# ['-1', '16', '12', '1', '17', '12', '2', '19', '15', '7', '-1', '13', '17', '-1', '13', '-1', '10', '11', '12', '-1']
# [1000000000000.0, 15, 17, 21, 17, 23, 20, 11, 15, 14, 8, 5, 14, 3, 9, 9, 9, 11, 21, 5]


# def dijkstra(g, source):
#     inf = 1e12
#     dis_node = nx.get_node_attributes(g, "dis")
#     n = g.number_of_nodes()
#     v = [0 for i in range(n)]
#     int_source = int(source)
#     dis = [inf for i in range(n)]
#     paths = ["-1" for i in range(n)]
#     v[int_source] = 1
#     for i in nx.neighbors(g, source):
#         dis[int(i)] = dis_node[str(i)]
#     for i in range(n):
#         k = 0
#         for j in range(n):
#             if not v[j] and (k is 0 or dis[j] < dis[k]):
#                 k = j
#         v[k] = 1
#         for j in nx.neighbors(g, str(k)):
#             index = int(j)
#             if not v[index] and dis[k] + dis_node.get(j) < dis[index]:
#                 dis[index] = dis[k] + dis_node.get(j)
#                 paths[index] = str(k)
#     print(paths)
#     print(dis)
#     return paths, dis