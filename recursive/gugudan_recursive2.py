def gugudan1(dan, depth):
    if depth > 9 :
        return

    print(dan, "*", depth, "=", dan*depth)
    gugudan1(dan, depth + 1)


dan = 2
gugudan1(dan, 9)