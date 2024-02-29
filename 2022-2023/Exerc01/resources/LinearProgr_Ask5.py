import numpy as np
import matplotlib.pyplot as plt
import itertools

A = np.array([[-3, 2, 8], [-1, 1, 3], [-2, 1, 8],
             [1, 0, 0], [0, 1, 0], [0, 0, 1]])

b = np.array([17, 9, 16,
              0, 0, 0])

# print(np.linalg.solve(A[:3][:3], b[:3][:3]))

solutions = set()
feasible_solutions = set()
degenerate_solutions = []
numOfSolutions = 0
for combination in zip(itertools.combinations(A, 3), itertools.combinations(b, 3)):
    # for each combination solve the problem
    solution = tuple(np.linalg.solve(combination[0], combination[1]))
    numOfSolutions += 1
    # print(solution)
    solutions.add(solution)  # can't add np.array in set

    # if (sum(n < 0 for n in (np.array(combination[0]).dot(solution)-combination[1])) == 0):

    # if any of the lines*solution-b>0
    if len(solutions) != numOfSolutions:
        degenerate_solutions.append(solution)


print("Feasible Solutions")
for solution in solutions:
    if (sum(n > 0 for n in (A[:3].dot(solution)-b[:3])) == 0) and (sum(n < 0 for n in (A[3:].dot(solution)-b[3:])) == 0):
        print(
            f"The solution {solution[0]:.3f} {solution[1]:.3f} {solution[2]:.3f} is in the feasible region")

print("Degenerate Solutions")
# for solution in solutions:
if len(degenerate_solutions) == 0:
    print(
        f"There are no degenerate solutions")
else:
    print(
        f"The solution {degenerate_solutions[:][0]:.3f} {degenerate_solutions[:][1]:.3f} {degenerate_solutions[:][2]:.3f} is degenerate")

# if (not all(solution)):  # check for 0 in solution
#     print(
#         f"The solution {solution[0]:.3f} {solution[1]:.3f} {solution[2]:.3f} is degenerate")

print("All Solutions")
for solution in solutions:
    print(f"{solution[0]:.3f} {solution[1]:.3f} {solution[2]:.3f}")

# print(solutions)
# i = 0
# numOfCombinations = np.factorial(6)/(np.factorial(3)**2)
# while i < numOfCombinations:

#     i += 1
# for i, x in enumerate(A):


print("t5 \n")
A = np.array([[-3, 2, 8, 1, 0, 0],
              [-1, 1, 3, 0, 1, 0],
              [-2, 1, 8, 0, 0, 1]])

b = np.array([17, 9, 16])
sol = list(itertools.combinations([0, 1, 2, 3, 4, 5], 3))
for i in sol:
    B1 = np.array(A[:, i[0]])
    B2 = np.array(A[:, i[1]])
    B3 = np.array(A[:, i[2]])
    Bc = np.array([B1, B2, B3])
    print(Bc)
