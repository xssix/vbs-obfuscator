import random
import string
import sys
import os
import argparse

def random_var(length=None):
    if length is None:
        length = random.randint(30, 60)
    chars = "lI1O0SZ5z2"
    first = random.choice("lIOsz")
    return first + "".join(random.choice(chars) for _ in range(length - 1))

def dynamic_key_engine(target_key, iterations=35):
    v_name = random_var(10)
    start_val = random.randint(100, 1000)
    ops = [f"Dim {v_name}", f"{v_name} = {start_val}"]
    curr = start_val
    for _ in range(iterations - 1):
        mode = random.choice(["+", "-", "Xor"])
        val = random.randint(10, 200)
        if mode == "+":
            curr += val
        elif mode == "-":
            curr -= val
        else:
            curr ^= val
        ops.append(f"{v_name} = {v_name} {mode} {val}")
    fix = curr ^ target_key
    ops.append(f"{v_name} = {v_name} Xor {fix}")
    return v_name, "\r\n".join(ops)

def obf_str(text):
    return " & ".join([f"Chr({ord(c)})" for c in text])

def obfuscate_vbs(source_code):
    k1 = random.randint(40, 250)
    p1 = "x".join([str(ord(c) ^ k1) for c in source_code])
    v_p = random_var()
    v_k = random_var()
    v_f = random_var()
    v_a = random_var()
    v_o = random_var()
    v_i = random_var()
    k1_var, k1_logic = dynamic_key_engine(k1, 40)
    inner_stub = f"""
On Error Resume Next
{k1_logic}
Dim {v_p}, {v_k}
{v_p} = "{p1}"
{v_k} = {k1_var}
Function {v_f}(d, k)
    Dim {v_a}, {v_o}, {v_i}
    {v_o} = ""
    {v_a} = Split(d, "x")
    For {v_i} = 0 To UBound({v_a})
        If {v_a}({v_i}) <> "" Then {v_o} = {v_o} & Chr(CInt({v_a}({v_i})) Xor k)
    Next
    {v_f} = {v_o}
End Function
Execute {v_f}({v_p}, {v_k})
""".strip()
    k2 = random.randint(50, 250)
    p2 = "x".join([str(ord(c) ^ k2) for c in inner_stub])
    o_f = random_var()
    o_p = random_var()
    o_k = random_var()
    o_a = random_var()
    o_o = random_var()
    o_i = random_var()
    k2_var, k2_logic = dynamic_key_engine(k2, 60)
    final_vbs = f"""
On Error Resume Next
{k2_logic}
Function {o_f}({o_p}, {o_k})
Dim {o_a}, {o_o}, {o_i}
{o_o} = ""
{o_a} = Split({o_p}, "x")
For {o_i} = 0 To UBound({o_a})
If {o_a}({o_i}) <> "" Then {o_o} = {o_o} & Chr(CInt({o_a}({o_i})) Xor {o_k})
Next
{o_f} = {o_o}
End Function
Execute {o_f}("{p2}", {k2_var})
""".strip()
    return final_vbs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-o", "--output")
    if len(sys.argv) == 1:
        sys.exit(1)
    args = parser.parse_args()
    output_file = args.output if args.output else "obfuscated.vbs"
    if not os.path.exists(args.input):
        sys.exit(1)
    with open(args.input, "r", encoding="utf-8") as f:
        src = f.read()
    obfuscated = obfuscate_vbs(src)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(obfuscated)
    print(f"File protected: {output_file}")

if __name__ == "__main__":
    main()
