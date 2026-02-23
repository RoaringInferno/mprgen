import numpy as np
from collections import namedtuple

def gen_matr(n=3,m=3,rng=5):
    A = np.random.normal(loc=0, scale=rng, size=(n, m))
    return np.round(A).astype(int)

def gen_problem(n=3, m=3, rng=5):
    A = gen_matr(n, m, rng)
    frob_norm = np.linalg.norm(A, 'fro')
    one_norm = np.linalg.norm(A, 1)
    two_norm = np.linalg.norm(A, 2)
    inf_norm = np.linalg.norm(A, np.inf)
    return Problem(A=A, frob=frob_norm, one=one_norm, two=two_norm, inf=inf_norm)

Problem = namedtuple("Problem", [ "A", "frob", "one", "two", "inf" ])

def display_matrix(A, zeroes="0", fmt="d", col_width=None):
    A = np.array(A)
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

def default_val(inp, val=4):
    if inp == "":
        return val
    else:
        return int(inp)
n = default_val(input("Row Count (Default=4): "))
m = default_val(input("Col Count (Default=4): "))
prblm = gen_problem(rng=9, n=n, m=m)
print("A = ")
display_matrix(prblm.A)
input("Enter for 1-norm ...")
print(prblm.one)
input("Enter for 2-norm ...")
print(prblm.two)
input("Enter for inf-norm ...")
print(prblm.inf)
input("Enter for Frobenius norm ...")
print(prblm.frob)

