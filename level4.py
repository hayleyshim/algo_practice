"""
#10818
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

n = int(input())
num = list(map(int, input().split()))
max = num[0]
min = num[0]

for i in num[1:]:
    if i > max:
       max = i
    elif i < min:
       min = i

print(min, max)

max, min을 정의하고 for문을 통해 비교하는 코드를 파이썬에서는 작성할 필요가 없다.
파이썬의 내장함수 min(), max()를 이용하면 최댓값과 최솟값을 편하게 구할 수 있다.

cnt =int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))
"""

"""
#2562
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램

num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)
"""
