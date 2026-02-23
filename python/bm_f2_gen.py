import random

def gen_word(n):
    return ''.join(random.choices(['0', '1'], k=n))

def format_binary_str(string, sep=" "):
    return sep.join(string[i:i+4] for i in range(0, len(string), 4))


def str_xor(a, b):
    A = (a == "1")
    B = (b == "1")
    if (A ^ B):
        return "1"
    else:
        return "0"

def str_and(a, b):
    A = (a == "1")
    B = (b == "1")
    if (A and B):
        return "1"
    else:
        return "0"

def row_map(A, B, func, n=-1):
    if (n == -1):
        n = max(len(A), len(B))
    rv = list()
    for i in range(n):
        a = A[i] if i < len(A) else "0"
        b = B[i] if i < len(B) else "0"
        rv.append(func(a, b))
    return rv

def row_and(A, B, n=-1):
    return row_map(A, B, str_and, n)

def row_xor(A, B, n=-1):
    return row_map(A, B, str_xor, n)

def gen_bm_table(word):
    n = len(word)
    q = [word]
    p = [['1']]
    D = [0]
    z = [-1]
    I = [0]
    j = word.find("1")
    for i in range(0, j):
        I.append(i+1)
        q.append(q[i][1:])
        p.append(['1']) # p_{i} := 1
        D.append(2*(i+1)) # D_i := 2i
        z.append(-1) # z_i := null
    I.append(j+1)
    p.append(['1']) # p_{j+1} := 1
    D.append(1) # D_{j+1} := 1
    z.append(j) # z_{j+1} := j
    q.append(q[j][1:])
    # print(p)
    for i in range(j+1, n):
        I.append(i+1)
        q_i_0 = q[-1][0]
        if (q_i_0 == "0"):
            q.append(q[i][1:])
        else:
            new_q = row_xor(q[i], q[z[i]], n-i)[1:]
            q.append(new_q)
        if (q_i_0 == "0") or (D[i] < D[z[i]]):
            D.append(2 + D[i])
            z.append(z[i])
        else:
            D.append(2 + D[z[i]])
            z.append(i)
        if (q_i_0 == "1"):
            p.append(
                    row_xor(
                        p[i], ["0"]*(i-z[i])+p[z[i]]
                        )
                    )
        else:
            p.append(p[i])
    return {
            "i": I,
            "q": q,
            "p": p,
            "D": D,
            "z": z
            }

def print_table(table):
    i_col = [ str(s) for s in table["i"] ]
    D_col = [ str(s) for s in table["D"] ]
    z_col = [ "-" if s==-1 else str(s) for s in table["z"] ]
    center_col = []
    for i in range(len(i_col)):
        q_str = "".join([ str(s) for s in table["q"][i] ])
        p_str = "".join([ str(s) for s in table["p"][i] ])
        center_str = q_str + "* " + p_str
        center_col.append(" ".join(center_str))
    max_i = max(len(s) for s in i_col)
    max_D = max(len(s) for s in D_col)
    max_z = max(len(s) for s in z_col)
    max_center = max(len(s) for s in center_col)
    print(f"q{"p":>{max_center-1}} | {"i":>{max_i}} | {"D":>{max_D}} | {"z":>{max_z}}")
    for i in range(len(i_col)):
        print(f"{center_col[i]:-<{max_center}} | {i_col[i]:>{max_i}} | {D_col[i]:>{max_D}} | {z_col[i]:>{max_z}}")

def print_register_table(layout, seed, n):
    reg_table = list()
    reg_table.append({
        "i": -1,
        "regs": list(seed[:len(layout)]),
        "out": -1,
        "feed": seed[len(layout)]
        })
    for i in range(0, n+3):
        prev_reg = reg_table[-1]["regs"]
        prev_feed = reg_table[-1]["feed"]
        new_reg = prev_reg[1:] + [str(prev_feed)]
        feedback = row_and(new_reg, layout).count("1") % 2
        reg_table.append({
            "i": reg_table[-1]["i"]+1,
            "regs": new_reg,
            "feed": feedback,
            "out": prev_reg[0]
            })
    i_col = list()
    reg_col = list()
    out_col = list()
    feed_col = list()
    for row in reg_table:
        i_col.append(str(row["i"]))
        reg_col.append(" ".join([ str(s) for s in row["regs"] ]))
        feed_col.append(str(row["feed"]))
        out_col.append(str(row["out"]) if row["out"] != -1 else "-")
    max_i = max(len(s) for s in i_col)
    max_regs = max([ len(s) for s in reg_col ] + [4])
    max_out = max([ len(s) for s in out_col ] + [3])
    max_feed = max([ len(s) for s in feed_col ] + [4])
    print(f"{"layout: ":>{max_i+3+max_out+3}}{" ".join(layout)}")
    print(f"{"k":>{max_i}} | {"out":>{max_out}} | {"regs":>{max_regs}} | {"feed":>{max_feed}}")
    for i in range(len(reg_table)):
        print(f"{i_col[i]:>{max_i}} | {out_col[i]:>{max_out}}{"*" if int(i_col[i])%4 == 0 else " "}| {reg_col[i]:>{max_regs}} | {feed_col[i]:<{max_feed}}")

problem = input("Word Size or Word: ")
if (len(problem) <= 2):
    problem = gen_word(int(problem.replace(" ", "")))
else:
    problem = "".join(problem.split(" "))
print(f"Word: {format_binary_str(problem)}")
input("Enter to reveal Berlekamp-Massey table...")
bm_table = gen_bm_table(problem)
print_table(bm_table)
input("Ender to reveal recurrence polynomial...")
recurrence_binary = bm_table["p"][-1][::-1]
print(f"{" + ".join([ "s(k+"+str(i)+")" for i, bin in enumerate(recurrence_binary) if bin=="1" ][::-1])} = 0")
input("Enter to reveal LFSR pattern...")
lfsr_pattern = recurrence_binary[:-1]
print(f"{format_binary_str("".join(lfsr_pattern))}")
input("Enter to reveal LFSR seed...")
print(f"{format_binary_str(problem[:len(lfsr_pattern)])} (First {len(lfsr_pattern)})")
print(f"feed_-1 := {problem[len(lfsr_pattern)]}")
input("Enter to reveal LFSR table...")
print_register_table(lfsr_pattern, problem, len(problem))
