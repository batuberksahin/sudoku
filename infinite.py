from random import choice

value = ["0 0 0 1 0 0 2 3 0", "0 2 4 0 0 0 0 0 0", "5 0 0 6 0 0 7 8 0"
         , "0 4 0 0 9 0 0 2 0", "0 0 7 0 8 0 6 0 0", "0 8 0 0 3 0 0 1 0"
         , "0 5 3 0 0 4 0 0 2", "0 0 0 0 0 0 3 5 0", "0 9 8 0 0 7 0 0 0"]

def sudoku():
    input = value + []
    for r in range(9):
        for c in range(9):
            v = input[r].split(' ')
            if v[c] == '0':
                p = '123456789'
                # Get Possibilities
                for rc in range(9):
                    if v[rc] != '0':
                        p = p.replace(v[rc], '')
                for cc in range(9):
                    cv = input[cc].split(' ')
                    if cv[c] != '0':
                        p = p.replace(cv[c], '')
                for bcr in range(3):
                    bcrv = input[(r // 3) * 3 + bcr].split(' ')
                    for bcc in range(3):
                        if bcrv[(c // 3) * 3 + bcc ] != '0':
                            p = p.replace(bcrv[(c // 3) * 3 + bcc], '')

                # Change item
                if p.__len__() != 0:
                    rand = choice(p)
                    input[r] = input[r][0:c * 2] + rand + input[r][c * 2 + 1:]
                    #print('ROW: ' + str(r + 1) + ' | COLUMN: ' + str(c + 1) + ' | POSS: ' + p + ' | INSERT: ' + rand)

    # Check table
    isBlank = False

    for r in range(9):
        for c in range(9):
            v = input[r].split(' ')
            if v[c] == '0':
                isBlank = True

    print(input)

    if isBlank:
        return True
    else:
        return False

attempt = 0

while True:
    if sudoku() == False:
        print('number of attempts: ' + str(attempt))
        break
    else:
        deneme = deneme + 1
        continue
