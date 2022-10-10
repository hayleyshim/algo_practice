# 버블 정렬, n(n-1)/2 , O(n^2) 느린 알고리즘

tmplist = [10, 2, 6, 4, 3, 7, 5]

"""first = tmplist[0]
second = tmplist[1]

print(first > second)

tmp = first
first = second
second = tmp

print(first, second)"""

for i in range(len(tmplist)):
    for j in range(i+1, len(tmplist)):
        if tmplist[i] > tmplist[j]:
            tmp = tmplist[i]
            tmplist[i] = tmplist[j]
            tmplist[j] = tmp
    print(tmplist)


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


