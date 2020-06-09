print("-" * 10, 1, "-" * 10)
a = int(input())
bin = f'{a:b}'
oct = f"{a:o}"
dec = f"{a:d}"
hex = f"{a:x}"
print(
    " " * (len(bin) - 3) + f"bin" + " " * 4 + \
    " " * (len(oct) - 3) + f"oct" + " " * 4 + \
    " " * (len(dec) - 3) + f"dec" + " " * 4 + \
    " " * (len(hex) - 3) + f"hex"
    )
print(
    " " * (3 - len(bin)) + f"{bin}" + " " * 4 + \
    " " * (3 - len(oct)) + f"{oct}" + " " * 4 + \
    " " * (3 - len(dec)) + f"{dec}" + " " * 4 + \
    " " * (3 - len(hex)) + f"{hex}"
)

print("-" * 10, 2, "-" * 10)
a = input().strip().lower().replace(r"\t", "").replace( r"\b", "").replace( r"\n", "").strip()
b = input().strip().lower().replace(r"\t", "").replace( r"\b", "").replace( r"\n", "").strip()
if a == b and ('@' in a and '@' in b) and ('.' in a and '.' in b):
    print("Ok!")
else:
    print("Error!")

print("-" * 10, 3, "-" * 10)
a = input()
b = input()
at = True
bt = True
for i in range(len(a)):
    if a[i] == a[-1 - i]:
        at = True
        continue
    else:
        at = False
        break
for i in range(len(b)):
    if b[i] == b[-1 - i]:
        bt = True
        continue
    else:
        bt = False
        break
print("Yes" if at and bt else "False")

print("-" * 10, 4, "-" * 10)
a = input()
b = input()
print(b[:len(b)//2] + a + b[len(b)//2:])

print("-" * 10, 5, "-" * 10)
a = input()
for i in a:
    if i.islower():
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")

print()
print("-" * 10, 6, "-" * 10)
a = input()
a = list(a)
dot = 0
if '.' in a:
    dot = a.count('.')
    a.remove('.')
a = ''.join(a)
if a.isnumeric() and dot and dot < 2:
    print("float")
elif a.isnumeric():
    print("int")
else:
    print("str")
