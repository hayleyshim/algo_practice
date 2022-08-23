"""
#2750

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

"""

N = int(input())
num_list = []

for i in range(N):
    num_list.append(int(input()))

ascending = sorted(num_list)

for i in range(len(ascending)):
    print(ascending[i])

