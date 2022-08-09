"""
#N) 2739

n = int(input())

for i in range(1,10):
    print(n, '*', i, '=', n*i)"""

"""
#N) 10950
t = int(input()) # 테스트 케이스 개수 t를 입력받음

for i in range(t): # t 만큼 반복
    a,b = map(int,input().split()) #split 함수를 이용해서 # 입력받은 값을 공백을 기준으로 분리 정수로 변환하기 위해서 map 함수를 이용하여 코드를 한 줄로 작성
    print(a+b)"""

"""
#8393
n = int(input())
sum = 0

for i in range(n+1):
    sum += i

print(sum)"""

"""
#11021
t = int(input()) # 테스트 케이스 개수 t를 입력받음

for i in range(t): # t 만큼 반복K
    a,b = map(int,input().split()) #split 함수를 이용해서 # 입력받은 값을 공백을 기준으로 분리 정수로 변환하기 위해서 map 함수를 이용하여 코드를 한 줄로 작성
    print("Case #", i+1, ":", a+b, sep='')
"""


#11022
t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
