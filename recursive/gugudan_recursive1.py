def gugudan1(dan, depth):
    if depth < 1 :
        return

    gugudan1(dan, depth-1)
    print(dan, "*", depth, "=", dan*depth)

dan = 2
gugudan1(dan, 9)