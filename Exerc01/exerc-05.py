import numpy as np
from itertools import combinations

def main():
    l = [   [-3,2,8,17],
            [-1,1,3,9],
            [-2,1,8,16],
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
         ]

    c = list(combinations(l,3))

    # results = []
    # for i,value in enumerate(c) :
    #     a = np.array([x[:3] for x in value])
    #     b = np.array([x[3] for x in value])
    #     x = np.linalg.solve(a,b)
    #     results.append(x)

    results = []
    for inde,value in enumerate(c) :
        a = np.array([x[:3] for x in value])
        b = np.array([x[3] for x in value])
        result = np.linalg.solve(a,b)
        results.append(result)
        print(f'{str(value[0]):14s} \n'+f'{str(value[1]):14s} = {result} \n'+f'{str(value[2]):14s} \n')



    # for inde,result in enumerate(results):
    #     print(f'{str(c[inde][0]):14s} \n'+f'{str(c[inde][1]):14s} = {result} \n'+f'{str(c[inde][2]):14s} \n')

if __name__ == "__main__":
    main()