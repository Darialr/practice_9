x = int(input())
k = 0
for i in range(1, int(x**0.5) + 1):
    for j in range(1, int(x**0.5) + 1):
        if i**2 + j**2 == x and (j >= i or j <= i):
            k += 1
print(k // 2)
