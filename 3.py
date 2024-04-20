n = int(input('Введите количество упаковок эскимо ->'))
if n % 2 == 0:
    answer = int(n / (n / 2))
    if answer >= 2:
        print(answer)
    else:
        print('слишком маленькая группа')
else:
    answer = []
    for i in range(3, 100):
        if n % i == 0:
            answer.append(i)
    print(answer[0])
