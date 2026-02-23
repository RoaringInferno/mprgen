import random
from collections import namedtuple
import math

def gen_base(mod):
    def gen():
        return random.randint(2, mod//2)
    rv = gen()
    while math.gcd(mod, rv) != 1:
        rv = gen()
    return rv
def gen_mod():
    return random.randint(11, 99)
def prob_gen():
    mod = gen_mod()
    return Parameters(mod=mod, base=gen_base(mod))

Parameters = namedtuple("Parameters", [ "mod", "base" ])


def gen_index_table(mod, base):
    values = [1]
    while True:
        new_val = values[-1]*base % mod
        if new_val == 1: break
        values.append(new_val)
    return values
def print_index_table(table):
    val_col = [ str(s) for s in table ]
    exp_col = [ str(s) for s in range(len(table)) ]
    max_val = max([ len(s) for s in val_col ] + [3])
    max_exp = max([ len(s) for s in exp_col ] + [3])
    print(f"{"exp":>{max_exp}} | {"val":>{max_val}}")
    for i in range(len(table)):
        print(f"{exp_col[i]:>{max_exp}} | {val_col[i]:>{max_val}}")
    return

Problem = namedtuple("Problem", [ "numer", "denom", "ans" ])
def gen_problem(table):
    def gen_exp():
        return random.randint(1,len(table)-1)
    ne = gen_exp()
    de = gen_exp()
    ae = ne-de
    return Problem( numer=table[ne], denom=table[de], ans=table[ae] )

params = Parameters(
        mod=input("Mod (Nothing for random): "),
        base=input("Base (Nothing for random): ")
        )
if (params.mod == "") and (params.base == ""):
    params = prob_gen()
elif params.mod == "":
    new_mod = gen_mod()
    while new_mod <= int(params.base):
        new_mod = gen_mod()
    params = Parameters(mod=new_mod, base=int(params.base))
elif params.base == "":
    new_base = gen_base(int(params.mod))
    params = Parameters(base=new_base, mod=int(params.mod))
else:
    params = Parameters(base=int(params.base), mod=int(params.mod))
if math.gcd(params.base, params.mod) != 1:
    print("Illegal base, randomly regenerating (not relatively prime)...")
    params = Parameters(mod=params.mod, base=gen_base(params.mod))
if params.base >= params.mod:
    print("Illegal base, randomly generating (>= mod)...")
    params = Parameters(mod=params.mod, base=gen_base(params.mod))

print(f"Mod = {params.mod}, Base = {params.base}")
input("Enter for index table...")
table = gen_index_table(params.mod, params.base) 
print_index_table(table)
pcount = input("Problem count (default 5): ")
if pcount == "": pcount = 5
else: pcount = int(pcount)
input("Enter for problems...")
problems = [ gen_problem(table) for _ in range(pcount) ]
i = 1
for prob in problems:
    print(f"{i}) {prob.numer} / {prob.denom} = ?")
    i += 1
input("Enter for solutions...")
i = 1
for prob in problems:
    print(f"{i}) {prob.ans}")
    i += 1
