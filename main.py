print('-'*10 + '1' + '-'*10)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 123, 32, 102]
for i in range(len(n)):
    if n[i] % 2:
        n[i] = n[i]**2
    else:
        n[i] = 0
print(n)

print('-'*10 + '2' + '-'*10)
n = [1, 1, 1, 2, 2, 0, 0, 3, 3, 3, 3]
for i in n:
    while n.count(i) > 1:
        n.remove(i)
print(n)

print('-'*10 + '3' + '-'*10)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 123, 32, 102]
max = n[0]
min = n[0]
for i in n:
    if max < i:
        max = i
    
    if min > i:
        min = i
print(max, min)

print('-'*10 + '4' + '-'*10)
n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 123, 32, 102]
n2 = [1, 1, 1, 2, 2, 0, 0, 3, 3, 3, 3]

for i in n1:
    for j in n2:
        if j == i:
            print(j, end=' ')
            break