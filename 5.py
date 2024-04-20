initial = []
for i in range(100000, 1000000):
    initial.append(i)

last_plndrm = []
for i in initial:
    if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2] and str(i)[2] == str(i)[-3]:
        last_plndrm.append(i)

third_plndrm = []
for i in last_plndrm:
    if str(i-1)[1] == str(i-1)[-2] and str(i-1)[2] == str(i-1)[-3]:
        third_plndrm.append(i-1)

second_plndrm = []
for i in third_plndrm:
    if str(i-1)[1] == str(i-1)[-1] and str(i-1)[2] == str(i-1)[-2]:
        second_plndrm.append(i-1)

first_plndrm = []
for i in second_plndrm:
    if str(i-1)[1] == str(i-1)[-1] and str(i-1)[2] == str(i-1)[-2]:
        first_plndrm.append(i-1)

print(*first_plndrm)