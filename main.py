from process_data.processing import process_data
from tensorly.decomposition import tucker, parafac, non_negative_parafac
from tensorly import kruskal_to_tensor
import tensorly as tl
import numpy as np
from time import time
from mfd_model import green_shields, green_berg, under_wood
from clustering.t_sne import t_sne

step = 2

step_dict = {
    1: "process_data",
    2: "analysis_network",
    3: "mfd_model_analysis",
    4: "clustering",
}


def main():
    step_func = step_dict.get(step)
    if step_func is "process_data":
        process_data()
    elif step_func is "analysis_network":
        # a = np.random.random(24).reshape((3,4,2))*24
        a = np.array([[[ 0, 21.27317725],
  [0, 23.94675626],
  [ 4.37572234, 0],
  [11.63075511,  8.22927049],],

 [[ 9.53826245, 7.72401752],
  [0, 2.01833392],
  [0, 5.81186906],
  [ 0.19812227, 0]],

 [[21.64887039, 0],
  [ 0,  0.30568754],
  [ 1.07547706, 0],
  [ 9.27505332, 18.09535406]]])
        print(a)
        print(a.ndim)
        factors = non_negative_parafac(a, rank=5)
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
    elif step_func is "clustering":
        t_sne()


if __name__ == '__main__':
    main()
