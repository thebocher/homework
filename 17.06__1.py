print('-' * 10, 1, '-' * 10)
def func1(l, n=1):
    new_l = []
    for _ in range(n):
        new_l.append(max(l))
        l.remove(max(l))
    return new_l
f = func1([1, 2, 3, 4], 2)
print(f)

print('-' * 10, 2, '-' * 10)
def func2(a, b):
    new_l = []
    if len(a) > len(b):
        for i in b:
            if i in a:
                new_l.append(i)
    else:
        for i in a:
            if i in b:
                new_l.append(i)
    return new_l

f = func2([1, 2, 3], [1, 3])
print(f)

print('-' * 10, 3, '-' * 10)
def func3(a):
    new_l = []
    for i in range(1, a):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count < 3:
            new_l.append(i)
    return new_l
f = func3(50)
print(f)

print('-' * 10, 4, '-' * 10)
def func4(d):
    keys = list(d.keys())
    keys.reverse()
    
    new_d = {}
    for key in keys:
        new_d[key] = d[key]
    return new_d

f = func4({1: 2, 2: 3})
print(f)

print('-' * 10, 5, '-' * 10)
def func5(s):
    new_d = {}
    s = s.lower()
    for i in s:
        new_d[i] = s.count(i)
    return new_d
f = func5('hello')
print(f)

print('-' * 10, 6, '-' * 10)
def func6(*a):
    print(a)
func6(1, 2, 3, 4)

print('-' * 10, 7, '-' * 10)
def func7(n, i=0):
    if not n:
        return i
    return func7(n-1, n-1+i)
print(func7(7))

print('-' * 10, 8, '-' * 10)
def func8(x):
    return -1 - x + x**2, (x**3) - 4 * (x**2) - 4 * x +1
f = func8(8)
print(f)

print('-' * 10, 9, '-' * 10)
def func9(a, b):
    return b / a
f = func9(10, 20)
print(f)

print('-' * 10, 10, '-' * 10)
def func10(a, b, c, d=0):
    c -= d 
    D = ((b**2) - 4 * a * c) ** 0.5
    if D > 0:
        x1 = (-b + D) / 2*a
        x2 = (-b - D) / 2*a
        return f'x1 = {x1}\nx2 = {x2}'
    elif D == 0:
        x = -b / 2*a
        return f'x1 = {x1}'
    else:
        return "(пуста множина)"
f = func10(1, 3, 2)
print(f)

print('-' * 10, 11, '-' * 10)
def func11(a, b, c, d=0):
    def func(x):
        nonlocal a, b, c, d
        abcdx = a*(x**2) + b*x + c
        print(abcdx)
    return func(int(input()))
f = func11(1, 3, 2)