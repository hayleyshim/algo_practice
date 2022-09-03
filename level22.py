"""
#11279
최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
입력되는 자연수는 231보다 작다.

입력에서 0이 주어진 회수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

힙 : 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리
최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
"""

import sys
import heapq

n = int(input())
heap = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,(-1)*a)
        # 넣어주는 값에 -1을 곱해 heap에 push를 해주면
        # 가장 큰 값이 음수가 되면 가장 작은 값이 되기 때문에 최대힙 구현이 가능
