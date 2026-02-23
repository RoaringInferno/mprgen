import random
from collections import namedtuple
import numpy as np
from math import gcd
from functools import reduce

def vector_gcd(v):
    v_int = [int(x) for x in v if x != 0]
    return reduce(gcd, v_int) if v_int else 1

def qr_delta_decomposition(A):
    A = np.array(A, dtype=int)
    n = A.shape[1]
    V = []
    Delta = []
    R = np.zeros((n, n), dtype=int)

    for j in range(n):
        v = A[:, j].copy()
        for i in range(j):
            denom = np.dot(V[i], V[i])
            if denom != 0:
                k = round(np.dot(A[:, j], V[i]) / denom)
                v -= k * V[i]
            else:
                k = 0
            R[i, j] = k
        d = vector_gcd(v)
        v //= d
        Delta.append(d)
        V.append(v)
        R[j, j] = d

    Q = np.column_stack(V)
    Delta = np.diag(Delta)
    return Q, Delta, R

def gen_problem(dim, rng=3):
    # A_ij \in [-dim*rng^2, dim*rng^2]
    # sig_ij = sqrt{dim}rng^2/3
    L = np.tril(np.random.randint(-rng, rng, size=(dim, dim)))
    np.fill_diagonal(L, 1)
    U = np.triu(np.random.randint(-rng, rng, size=(dim, dim)))
    for i in range(dim):
        if U[i, i] == 0:
            U[i, i] = np.random.randint(1, rng + 1) if np.random.rand() > 0.5 else -np.random.randint(1, rng + 1)
    A = L @ U
    Q, Delta, R = qr_delta_decomposition(A)
    return Problem(A=A, r=R, q=Q, Delta=Delta)

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

Problem = namedtuple("Problem", { "A", "r", "q", "Delta" })

dim_in = input("Dimension (Default 4):")
prblm = gen_problem(4)
if dim_in != "":
    prblm = gen_problem(int(dim_in))
print("A matrix:")
display_matrix(prblm.A, zeroes=".")
input("Enter for q ...")
display_matrix(prblm.q, zeroes=".")
input("Enter for Delta ...")
display_matrix(prblm.Delta, zeroes=" ")
input("Enter for r ...")
display_matrix(prblm.r, zeroes=" ")
