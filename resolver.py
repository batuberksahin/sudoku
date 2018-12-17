def resolve(input: list):
    for restart in range(9):
        for a in range(9):
            for i in range(9):
                l = input[a].split(' ')
                if l[i] == '0':
                    poss = '123456789'
                    # Lane check
                    for m in range(9):
                        if l[m] != '0':
                            poss = poss.replace(l[m], '')
                    # Column check
                    for c in range(9):
                        k = input[c].split(' ')
                        if k[i] != '0':
                            poss = poss.replace(k[i], '')
                    # Block lane check
                    for bl in range(3):
                        blk = input[(a // 3) * 3 + bl].split(' ')
                        for bc in range(3):
                            if blk[(i // 3) * 3 + bc] != '0':
                                poss = poss.replace(blk[(i // 3) * 3 + bc], '')

                    print('row: ' + str(a+1) + ' | col: ' + str(i+1) + ' | poss: ' + poss)

                    # Insert value
                    if poss.__len__() == 1:
                        print('chosen value: ' + poss)
                        input[a] = input[a][0:i*2] + poss + input[a][i*2+1:]
    return input
