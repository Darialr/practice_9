n, d, r = map(int, input('Ввведите количество колец, толщину и радиус->').split())


def lengh(a, b, c):
    one = 2 * b + 2 * c
    if a % 2 == 0:
        result = one * (((a - 1) // 2) + 1) + (c - 2) * 2 * ((a - 1) // 2) + (one - 4)
    else:
        result = one * ((a // 2) + 1) + (c - 2) * 2 * (a // 2)
    return result


print(lengh(n, d, r))
