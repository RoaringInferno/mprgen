import random
from collections import namedtuple

def factor(divisor, dividend):
    q = dividend // divisor
    r = dividend % divisor
    return factor.Result(divisor, dividend, q, r)
factor.Result = namedtuple("Result", ["divisor", "dividend", "quotient", "remainder"])

def gen_num():
    return random.randint(2, 10**3)

def prob_gen():
    a = gen_num()
    b = gen_num()
    while a == b:
        b = gen_num()
    return prob_gen.Result(min(a, b), max(a, b))
prob_gen.Result = namedtuple("Result", ["divisor", "dividend"])

def gen_eea_table(divisor, dividend):
    rows = []
    r0, r1 = dividend, divisor
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r2 = r0 - q * r1
        s2 = s0 - q * s1
        t2 = t0 - q * t1
        rows.append(gen_eea_table.Row(r2, q, s2, t2))
        r0, r1 = r1, r2
        s0, s1 = s1, s2
        t0, t1 = t1, t2
    return gen_eea_table.Table(divisor, dividend, rows)
gen_eea_table.Row = namedtuple("Row", ["r", "q", "s", "t"])
gen_eea_table.Table = namedtuple("Table", ["divisor", "dividend", "rows"])

def print_eea_table(table):
    r_col = [str(s) for s in [table.dividend, table.divisor] +[row.r for row in table.rows] ]
    q_col = [str(s) for s in ["", ""] + [row.q for row in table.rows] ]
    s_col = [str(s) for s in ["1", "0"] + [row.s for row in table.rows] ]
    t_col = [str(s) for s in ["0", "1"] + [row.t for row in table.rows] ]
    D_col = [str(s) for s in ["", "", table.dividend, table.divisor] + [row.r for row in table.rows[:-2]] ]
    d_col = [str(s) for s in ["", "", table.divisor] + [row.r for row in table.rows] ]
    max_r = max(len(s) for s in r_col)
    max_q = max(len(s) for s in q_col)
    max_s = max(len(s) for s in s_col)
    max_t = max(len(s) for s in t_col)
    max_D = max(len(s) for s in D_col)
    max_d = max(len(s) for s in d_col)
    print(f"{"D":>{max_D}}   {"q":>{max_q}}   {"d":>{max_d}}   {"r":>{max_r}} | {"s":{max_s}} | {"t":{max_t}}")
    for i in range(0,2):
        print(f"{D_col[i]:>{max_D}}   {q_col[i]:>{max_q}}   {d_col[i]:>{max_d}}   {r_col[i]:>{max_r}} | {s_col[i]:{max_s}} | {t_col[i]:{max_t}}")
    for i in range(2,len(table.rows)+2):
        print(f"{D_col[i]:>{max_D}} = {q_col[i]:>{max_q}} * {d_col[i]:>{max_d}} + {r_col[i]:>{max_r}} | {s_col[i]:{max_s}} | {t_col[i]:{max_t}}")

problem = prob_gen.Result(
        dividend=input("Dividend (Nothing for random): "),
        divisor=input("Divisor (Nothing for random): ")
        )
if (problem.divisor == "") and (problem.dividend == ""):
    problem = prob_gen()
elif (problem.divisor == ""):
    new_divisor = gen_num()
    while new_divisor > problem.dividend:
        new_divisor = gen_num()
    problem = prob_gen.Result(divisor=new_divisor, dividend=int(problem.dividend))
elif (problem.dividend == ""):
    new_dividend = gen_num()
    while new_dividend <= problem.divisor:
        new_dividend = gen_num()
    problem = prob_gen.Result(dividend=new_dividend, divisor=int(problem.divisor))
else:
    problem = prob_gen.Result(dividend=int(problem.dividend), divisor=int(problem.divisor))
print(f"{problem.divisor} into {problem.dividend}")
input("Enter for EEA table...")
table = gen_eea_table(problem.divisor, problem.dividend)
print_eea_table(table)
