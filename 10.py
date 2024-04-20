def ways(a, b):
    if a == 0:
        return 1
    if a < 0 or b == 0:
        return 0
    return ways(a - b, b - 1) + ways(a, b - 1)


k = int(input("Введите количество кубиков -> "))
print(ways(k, k))
