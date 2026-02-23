import numpy as np
from collections import namedtuple

def gen_inverse(n=3, rng=3, depth=20):
    A = np.eye(n, dtype=int)
    Ainv = np.eye(n, dtype=int)
    for _ in range(depth):
        op_type = np.random.choice(['add', 'add', 'swap', 'neg'])
        if op_type == 'add':
            i, j = np.random.choice(n, 2, replace=False)
            k = np.random.randint(-rng, rng + 1)
            A[i] += k * A[j]
            Ainv[:, j] -= k * Ainv[:, i]  # inverse operation
        elif op_type == 'swap':
            i, j = np.random.choice(n, 2, replace=False)
            A[[i,j]] = A[[j,i]]
            Ainv[:, [i,j]] = Ainv[:, [j,i]]
        elif op_type == 'neg':
            i = np.random.randint(n)
            A[i] *= -1
            Ainv[:, i] *= -1
    return A, Ainv

def display_matrix(A, zeroes="0", fmt="d", col_width=None):
    A = np.array(A)  # ensure array
    n_rows, n_cols = A.shape
    if col_width is None:
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

def deflt(inp, val=3):
    if inp == "":
        return val
    else:
        return int(inp)

n = deflt(input("Square Matrix Dimension (Default=3): "))
A, B = gen_inverse(n=n)
display_matrix(A)
input("Enter for inverse ...")
display_matrix(B)
