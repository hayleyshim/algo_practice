def diagonaltravel(x, y):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, -1, 1, 1, 1, 0, -1, -1]

    data = [[0 for _ in range(5)] for _ in range(5)]
    data[x][y] = 1
    printList(data)

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        print(x, y, nx, ny)
        if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
            data[nx][ny] = 1


    return data

def printList(sample):
    for ary in sample:
        for c in ary:
            print(c, end=" ")
        print()
    print()


print("대각선 값 채우기")
x = 2
y = 2
res1 = diagonaltravel(x, y)
printList(res1)