"""
#10818
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
"""
"""
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
"""

"""
cnt =int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))
"""



