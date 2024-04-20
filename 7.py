for s in range(0, 10):
    for e in range(0, 10):
        for n in range(0, 10):
            for d in range(0, 10):
                for m in range(1, 10):
                    for o in range(0, 10):
                        for r in range(0, 10):
                            for y in range(0, 10):
                                if (s != e and s != n and s != d and s != m and s != o and s != r and s != y and
                                        e != n and e != d and e != m and e != o and e != r and e != y and
                                        n != d and n != m and n != o and n != r and n != y and
                                        d != m and d != o and d != r and d != y and
                                        m != o and m != r and m != y and o != r and o != y and r != y):
                                    if int(f'{s}{e}{n}{d}') + int(f'{m}{o}{r}{e}') == int(f'{m}{o}{n}{e}{y}'):
                                        print(f'{s}{e}{n}{d} + {m}{o}{r}{e} = {m}{o}{n}{e}{y}')
