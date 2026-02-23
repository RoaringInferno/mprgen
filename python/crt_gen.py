import random
from collections import namedtuple

primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71 ] # First 20 primes
primes_to_use = 10

def gen_rel_primes(n, max_value=20):
    rv = [ 1 for _ in range(n) ]
    max_exponent = max(2 // n, 1)
    exponents = [ random.randint(0,max_exponent) for _ in range(primes_to_use) ]
    assignment = [ random.randint(0,n-1) for _ in range(primes_to_use) ]
    for rk in range(primes_to_use):
        k = primes_to_use - 1 - rk
        new_value = rv[assignment[k]]
        for j in range(exponents[k]):
            new_value *= primes[k]
            if new_value >= max_value:
                new_value /= primes[k]
                break
        rv[assignment[k]] = int(new_value)
    # Ensure none are 1
    for i in range(n):
        if rv[i] == 1:
            for rk in range(primes_to_use):
                k = primes_to_use - 1 - rk
                if exponents[k] == 0:
                    rv[i] = primes[k]
                    exponents[k] = 1
                    assignment[k] = i
                    break
    return rv

def bezout_coefficients(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r != 1:
        raise ValueError(f"{a} and {b} are not coprime, gcd={old_r}")
    # old_r is gcd(a,b); coefficients: old_s * a + old_t * b = old_r
    # print(f"{old_s}*{a} + {old_t}*{b} = 1")
    return old_s, old_t


def gen_prob(rel_primes):
    prod = 1
    for prime in rel_primes: prod *= prime
    def get_coeff(prime):
        other = prod//prime
        a, b = bezout_coefficients(prime, other)
        return b*other
    equations = [
                gen_prob.Equation(
                    mod=prime,
                    value=random.randint(1, prime-1),
                    solution=get_coeff(prime)
                    )
                for prime in rel_primes
                ]
    return equations
gen_prob.Equation = namedtuple("Equation", ["mod", "value", "solution"])

def print_prob(prob):
    for eq in prob:
        print(f"x = {eq.value} (mod {eq.mod})")

def print_sol(prob):
    prod = 1
    for eq in prob: prod *= eq.mod
    def make_pos(num):
        while num < 0: num += prod
        return num
    ans = 0
    for eq in prob:
        ans += eq.value * eq.solution
        print(f"{make_pos(eq.solution)} = 1 (mod {eq.mod}); 0 (mod {prod//eq.mod})")
    print(f"Solution: {make_pos(ans)}")

count = input("Equation count (Nothing for random): ")
if count == "": count = random.randint(2, 4)
else: count = int(count)
primes = gen_rel_primes(count, 80//count)
problem = gen_prob(primes)
print_prob(problem)
input("Enter for solution...")
print_sol(problem)
