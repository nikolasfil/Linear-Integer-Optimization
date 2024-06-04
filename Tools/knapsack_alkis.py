from scipy.optimize import linprog
import numpy as np


# Συνάρτηση που λύνει το πρόβλημα σακιδίου
def solve_knapsack(c, A, b, bounds):
    result = linprog(-c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    if result.success:
        return result.fun, result.x
    else:
        return None, None


# Αρχικά δεδομένα
c = np.array([23, 17, 30, 14, 9])
A = np.array([[6, 5, 10, 7, 5]])
b = np.array([14])
bounds = [(0, 1) for _ in range(len(c))]

# Αρχική λύση
best_value, best_solution = solve_knapsack(c, A, b, bounds)
if best_value is not None:
    best_value = -best_value  # αντιστροφή του αρνητικού σκοπού
    print(f"Initial continuous solution: {best_solution}, value: {best_value}")

# Λίστα κόμβων για διακλάδωση (value, bounds)
nodes = [(-best_value, bounds, best_solution)]
final_solution = None
final_value = -np.inf

while nodes:
    # Επιλέγουμε τον κόμβο με την καλύτερη τιμή (best-first)
    nodes = sorted(nodes, key=lambda x: x[0])
    current_value, current_bounds, current_solution = nodes.pop()
    current_value = -current_value  # αντιστροφή του αρνητικού σκοπού

    # Ελέγχουμε αν η λύση είναι ακέραια
    integer_solution = True
    for i in range(len(current_solution)):
        if not (current_solution[i] == 0 or current_solution[i] == 1):
            integer_solution = False
            # Διακλάδωση σε xi = 0 και xi = 1
            new_bounds_zero = current_bounds[:]
            new_bounds_zero[i] = (0, 0)
            new_bounds_one = current_bounds[:]
            new_bounds_one[i] = (1, 1)

            # Λύνουμε τα υποπροβλήματα
            val_zero, sol_zero = solve_knapsack(c, A, b, new_bounds_zero)
            if val_zero is not None:
                val_zero = -val_zero
                if val_zero > final_value:
                    nodes.append((-val_zero, new_bounds_zero, sol_zero))

            val_one, sol_one = solve_knapsack(c, A, b, new_bounds_one)
            if val_one is not None:
                val_one = -val_one
                if val_one > final_value:
                    nodes.append((-val_one, new_bounds_one, sol_one))
            break

    if integer_solution and current_value > final_value:
        final_solution = current_solution
        final_value = current_value

print(f"Final solution: {final_solution}, value: {final_value}")
