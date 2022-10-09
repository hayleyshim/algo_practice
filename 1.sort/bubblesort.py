# 버블 정렬

tmplist = [10, 2, 6, 4, 3, 7, 5]

for i in range(len(tmplist)):
    for j in range(len(tmplist)-1):
        if tmplist[j] > tmplist[j+1]:
            tmp = tmplist[j]
            tmplist[j] = tmplist[j+1]
            tmplist[j+1] = tmp
    print(tmplist)

print('------------------------------------')

tmplist = [10, 9, 2, 8 ,4, 3]

for i in range(len(tmplist)):
    for j in range(len(tmplist)-1):
        if tmplist[j] > tmplist[j+1]:
            tmp = tmplist[j]
            tmplist[j] = tmplist[j+1]
            tmplist[j+1] = tmp
    print(tmplist)