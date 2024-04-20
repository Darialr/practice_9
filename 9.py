n = int(input())
k = 0
for i in range(0, n + 1):
    for n in range(i, n + 1):
        k += i + n
print(k)
