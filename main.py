from process_data.processing import process_data, correct_data, get_all_tensor, get_visual_json_data
from tensorly.decomposition import tucker, parafac, non_negative_parafac
from tensorly import kruskal_to_tensor
import tensorly as tl
import numpy as np
from time import time
from mfd_model import green_shields, green_berg, under_wood

step = 1

step_dict = {
    1: "process_data",
    2: "analysis_network",
    3: "mfd_model_analysis"
}


def main():
    step_func = step_dict.get(step)
    if step_func is "process_data":
        # process_data()
        # correct_data()
        # get_all_tensor()
        # draw_data()
        get_visual_json_data()
    elif step_func is "analysis_network":
        # a = np.random.random(24).reshape((3,4,2))*24
        a = np.array([[[ 1.65507223, 21.27317725],
  [13.27929529, 23.94675626],
  [ 4.37572234, 16.79368879],
  [11.63075511,  8.22927049],],

 [[ 9.53826245, 7.72401752],
  [21.55269292, 2.01833392],
  [20.79722731, 5.81186906],
  [ 0.19812227, 17.57124187]],

 [[21.64887039, 16.64826073],
  [ 6.66237529,  0.30568754],
  [ 1.07547706, 16.62781564],
  [ 9.27505332, 18.09535406]]])
        print(a)
        print(a.ndim)
        factors = parafac(a, rank=5)
        # factors = non_negative_parafac(a, rank=5)
        for i in factors:
            print(i)
        print(tl.kruskal_to_tensor(factors))
        # d, c = tucker(a, ranks=[3,4,2])
        # print("*" * 30)
        # print(d)
        # print("*" * 30)
        # print(c)
        # print("*" * 30)
        # print(tl.tucker_to_tensor((d,c)))
    elif step_func is "mfd_model_analysis":
        under_wood.draw()



if __name__ == '__main__':
    main()
