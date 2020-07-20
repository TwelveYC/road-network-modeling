import networkx as nx
import requests
from xml.dom.minidom import parseString
from process_data.processing import process_data

step = 2

step_dict = {
    1: "process_data",
    2: "analysis_network"
}


def main():
    step_func = step_dict.get(step)
    if step_func is "process_data":
        process_data()
    elif step_func is "analysis_network":
        # 节点数：15458 边数：20946 有属性：10523
        pass
if __name__ == '__main__':
    main()