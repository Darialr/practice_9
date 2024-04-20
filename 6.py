for a in range(1, 10):
    for b in range(0, 10):
        AB = a * 10 + b
        CAB = AB * AB
        if CAB < 1000 and CAB % 100 == AB:
            print(CAB)
