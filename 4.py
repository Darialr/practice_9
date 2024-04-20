teams = 0
ropes = int(input())
while ropes != 0:
    if ropes % 4 == 0:
        teams += 1
    ropes = int(input())
print(teams)
