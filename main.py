import networkx as nx
import requests
from xml.dom.minidom import parseString
from process_data.processing import process_data, correct_data, get_all_tensor

step = 1

step_dict = {
    1: "process_data",
    2: "analysis_network"
}


def main():
    step_func = step_dict.get(step)
    if step_func is "process_data":
        # process_data()
        # correct_data()
        get_all_tensor()
    elif step_func is "analysis_network":
        pass


if __name__ == '__main__':
    main()