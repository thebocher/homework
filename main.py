print("-" * 10, 1, "-" * 10)
a = int(input())
print("bin\toct\tdec\thex")
print( "  {0:b}\t  {0:o}\t  {0:d}\t  {0:x}".format(a) )

print("-" * 10, 2, "-" * 10)
a = input().strip().lower().replace(r"\t", "").replace( r"\b", "").replace( r"\n", "").strip()
b = input().strip().lower().replace(r"\t", "").replace( r"\b", "").replace( r"\n", "").strip()
if a == b:
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

print("-" * 10, 6, "-" * 10)
a = input()
dot = a.count('.')
a = list(a)
a.remove('.')
a = ''.join(a)
if a.isnumeric() and dot and dot < 2:
    print("float")
elif a.isnumeric():
    print("int")
else:
    print("str")
