"""
#2798
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

"""

N, M = map(int, input().split())
num = list(map(int, input().split()))
l = len(num)
answer = 0

for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if(num [i] + num [j] + num [k] > M):
                continue
            else:
                answer = max(answer, num[i]+num[j]+num[k])
print(answer)


#itertools library
from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

permutationArray = permutations(num, 3)
ans = 0
for i in permutationArray:
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
print(ans)

