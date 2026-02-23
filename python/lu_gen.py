import random
from collections import namedtuple
import numpy as np


def gen_problem(dim=4, rng=7):
    # A_ij \in [-dim*rng^2, dim*rng^2]
    # sig_ij = sqrt{dim}rng^2/3
    L = np.tril(np.random.randint(-rng, rng, size=(dim, dim)))
    np.fill_diagonal(L, 1)
    U = np.triu(np.random.randint(-rng, rng, size=(dim, dim)))
    for i in range(dim):
        if U[i, i] == 0:
            U[i, i] = np.random.randint(1, rng + 1) if np.random.rand() > 0.5 else -np.random.randint(1, rng + 1)
    return Problem(A=L@U, L=L, U=U)

def display_matrix(A, zeroes="0", fmt="d", col_width=None):
    A = np.array(A)  # ensure array
    n_rows, n_cols = A.shape

    # Determine column width if not provided
    if col_width is None:
        # Treat zeros as zero_char for width calculation
        col_width = max(len(f"{x:{fmt}}" if x != 0 else str(zeroes)) for x in A.flatten())

    for i in range(n_rows):
        row_str = "[ "
        for j in range(n_cols):
            val = A[i, j]
            if val == 0:
                row_str += f"{zeroes:>{col_width}} "
            else:
                row_str += f"{val:{col_width}{fmt}} "
        row_str += "]"
        print(row_str)

Problem = namedtuple("Problem", { "A", "L", "U" })

def gen():
    dim_in = input("Dimension (Default 4):")
    prblm = gen_problem(dim=4)
    if dim_in != "":
        prblm = gen_problem(int(dim_in))
    print("A matrix:")
    display_matrix(prblm.A, zeroes=".")
    input("Enter for L ...")
    display_matrix(prblm.L, zeroes=" ")
    input("Enter for U ...")
    display_matrix(prblm.U, zeroes=" ")

gen()
# for _ in range(5):
#     prblm = gen_problem(rng=7, dim=4)
#     display_matrix(prblm.A)
#     print()
