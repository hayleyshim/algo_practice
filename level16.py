"""
#11659
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

시간 복잡도를 낮출 적절한 알고리즘 : prefix_sum
prefix_sum을 사용하지 않고 구현할 때
N, M의 입력 범위가 100,000이 넘어간다면 시간 복잡도는 O(NM)이 되므로 1초 내에 구현할 수가 없다.
"""

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in arr:
    temp += i
    prefix_sum.append(temp)

for i in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])
