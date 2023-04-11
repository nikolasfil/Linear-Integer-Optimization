import numpy as np
from itertools import combinations

def inequality(li, result):
    return sum([x*y for x,y in zip(li[:3],result)]) <= li[3]

def presenting(li):
    """Presenting the equation in a nice way"""

    result = ''
    # for i in range(3):
    if li[0] != 0:
        if li[0] == -1:
            result += '-'
        elif li[0] != 1:
            result += str(li[0])
        result += 'x1'
        if li[1]>0:
            result += '+'

    if li[1] != 0:
        if li[1] == -1:
            result += '-'
        elif li[1] != 1:
            result += str(li[1])
        result += 'x2' 
        if li[2]>0:
            result += '+'

    if li[2] != 0:
        if li[2] == -1:
            result += '-'
        elif li[2] != 1:
            result += str(li[2])
        result += 'x3'

    return f'{result} = {li[3]}'
   
def system(value):
    a = np.array([x[:3] for x in value])
    b = np.array([x[3] for x in value])

    # solve the system of equations
    return np.linalg.solve(a,b)

def main():
    # constraints from equations 1:3 and the second part of the equation 
    A = [   [-3,2,8,17],
            [-1,1,3,9],
            [-2,1,8,16],
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
         ]

    # get all combinations of 3 equations
    c = list(combinations(A,3))

    results = []

    print(f'\n\n{"-"*15}All{"-"*15}\n\n')

    for inde,value in enumerate(c) :
        result = system(value)
        results.append(result)

        print()
        print('\n'.join([f'{presenting(value[0]):17s} |',f'{presenting(value[1]):17s} | => {result} ',f'{presenting(value[2]):17s} |\n']))


    print(f'\n\n{"-"*15}valid{"-"*15}\n\n')

    for inde,value in enumerate(c) :
        # check if the result is valid with all 6 equations
        if all([inequality(x,results[inde]) for x in A[:3]]) and all([x>=0 for x in results[inde]]):
            print()
            print('\n'.join([f'{presenting(value[0]):17s} |',f'{presenting(value[1]):17s} | => {results[inde]} ',f'{presenting(value[2]):17s} |\n']))



if __name__ == "__main__":
    main()