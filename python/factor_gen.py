from collections import namedtuple
import numpy as np

def poly_to_string(coeffs):
    coeffs = np.array(coeffs)
    degree = len(coeffs) - 1
    terms = []
    
    for i, coef in enumerate(coeffs):
        power = degree - i
        if np.isclose(coef, 0):
            continue
        if np.isclose(coef, round(coef)):
            coef = int(round(coef))
        if coef > 0 and terms:
            sign = " + "
        elif coef < 0:
            sign = " - " if terms else "-"
        else:
            sign = ""
        
        abs_coef = abs(coef)
        if power == 0:
            term = f"{abs_coef}"
        elif power == 1:
            term = "x" if abs_coef == 1 else f"{abs_coef}x"
        else:
            term = f"x^{power}" if abs_coef == 1 else f"{abs_coef}x^{power}"
        
        terms.append(sign + term)
    
    return "".join(terms) if terms else "0"

def gen_problem(n=2, rng=9):
    roots = np.random.randint(-rng, rng, size=n)
    factors = []
    for r in roots:
        if r == 0:
            factors.append("(x)")
        elif r > 0:
            factors.append(f"(x - {r})")
        else:
            factors.append(f"(x + {abs(r)})")
    poly = np.poly(roots)
    poly_str = poly_to_string(poly)
    return Problem(poly=poly_str, factors=factors)
Problem = namedtuple("Problem", [ "poly", "factors" ])

degree = input("Degree (Default = 2)? ")
if degree == "": degree = 2
else: degree = int()
count = input("How many (Default = 5)? ")
if count == "": count = 5
else: count = int()

prblms = [ gen_problem() for _ in range(count) ]
for i, prblm in enumerate(prblms): print(f"{i+1}: {prblm.poly}")
input("Enter for solutions ...")
for i, prblm in enumerate(prblms): print(f"{i+1}: {prblm.factors}")
