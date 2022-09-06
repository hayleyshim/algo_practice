"""
#14425

총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
"""

s = set()
count = 0

N, M = map(int, input().split())

for _ in range(N):
    data = input().rstrip()
    s.add(data)


for _ in range(M):
    data = input().rstrip()
    if data in s:
        count += 1

print(count)

#10815
"""
상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성
binary search()
"""
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')


input()
card = set(map(int, input().split()))

input()
own = list(map(int, input().split()))

for i in own:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')