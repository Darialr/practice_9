n, d, r = map(int, input('Ввведите количество колец, толщину и радиус->').split())


def lengh(a, b, c):
    one = 2 * b + 2 * c
    if a % 2 == 0:
        whole = one * n - (2 * b) * ((a / 2) - 1)
    else:
        whole = one * n - (2 * b) * ((a // 2) + 1)
    return whole


print(lengh(n, d, r))
