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

#2751
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성

시간복잡도 O(nlogn)

1. 파이썬 내장함수 사용(sorted)

2. 퀵정렬

3. 퀵정렬(cache사용없이)

4. 병합정렬

5. 힙정렬
"""
#sorted
#병합정렬을 기반으로 만들어진 함수이며 O(nlogn)의 시간복잡도를 가지는 알고리즘
import sys

n = int(input())
li = []

for i in range(n):
    li.append(int(sys.stdin.readline()))

for i in sorted(li):
    print(i)

#quick_sort
#퀵정렬은 시간초과는 안떳는데 메모리초과 오류
#퀵정렬 함수가 재귀로 돌아갈때마다 bigger, smaller 리스트가 생성되어 cache메모리를 많이 차지하기

import sys
def quick_sort(li):
    length = len(li)
    if length <= 1:
        return li
    else:
        pivot=li[0]
        bigger = [ele for ele in li[1:] if ele > pivot]
        smaller = [ele for ele in li[1:] if ele < pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)

n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li = quick_sort(li)

for i in li:
    print(i)

#merge 1.sort
# 병합정렬은 어떤 상황에서도 O(nlogn)의 시간복잡도를 보장
# O(nlogn)의 시간복잡도를 가지니 안정성 부분에서는 더 좋다
# Merge Sort
def merge(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge(array[:mid])
    right = merge(array[mid:])

    return merge_func(left, right)


def merge_func(left, right):
    merge_list = []
    left_id, right_id = 0, 0

    # case1 left, right
    while len(left) > left_id and len(right) > right_id:
        if left[left_id] > right[right_id]:
            merge_list.append(right[right_id])
            right_id += 1
        else:
            merge_list.append(left[left_id])
            left_id += 1

    # case2 letf
    while len(left) > left_id and len(right) <= right_id:
        merge_list.append(left[left_id])
        left_id += 1

    # case3 right
    while len(right) > right_id and len(left) <= left_id:
        merge_list.append(right[right_id])
        right_id += 1

    return merge_list


import sys

n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li = merge(li)

for i in li:
    print(i)


#heap 1.sort
# 병합정렬과 같이 시간복잡도 O(nlogn)을 보장하는 정렬 알고리즘

import heapq

def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, value)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

import sys
n = int(input())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

li = heapsort(li)
for i in li:
    print(i)


