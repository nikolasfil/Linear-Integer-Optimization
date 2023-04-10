import numpy as np
from itertools import combinations

def presenting(li):
    return  f"{str(li[0] if li[0]!=1 else '')+'x1' if li[0]!=0 else '' }"+f"{'+' if li[1]>0 else ''}" +\
            f"{str(li[1] if li[1]!=1 else '')+'x2' if li[1]!=0 else '' }"+f"{'+' if li[2]>0 else ''}" +\
            f"{str(li[2] if li[2]!=1 else '')+'x3' if li[2]!=0 else '' }" + f"={li[3]}"

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
        if np.allclose(np.dot(a, result), b):
           results.append(result)
        # print(f'{str(value[0]):14s} \n'+f'{str(value[1]):14s} = {result} \n'+f'{str(value[2]):14s} \n')
        print('\n'.join([f'{presenting(value[0]):14s} ',f'{presenting(value[1]):14s} => {result} ',f'{presenting(value[2]):14s} \n']))

    print(len(results))


    # for inde,result in enumerate(results):
    #     print(f'{str(c[inde][0]):14s} \n'+f'{str(c[inde][1]):14s} = {result} \n'+f'{str(c[inde][2]):14s} \n')

if __name__ == "__main__":
    main()