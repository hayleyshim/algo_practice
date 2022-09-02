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

"""
#11022
t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
"""

"""
#10951

while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)
"""

#10952

while True:
    a, b = map(int, input().split())

    if(a == 0 and b == 0):
        break
    else:
        print(a + b)

#25304
"""
영수증에 적힌,

- 구매한 각 물건의 가격과 개수
- 구매한 물건들의 총 금액

을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사

첫째 줄에는 영수증에 적힌 총 금액 $X$가 주어진다.

둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 $N$이 주어진다.

이후 $N$개의 줄에는 각 물건의 가격 $a$와 개수 $b$가 공백을 사이에 두고 주어진다.

"""

x = int(input())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

sum = 0

for i in range(n):
    sum += arr[i][0]*arr[i][1] # 0번 상품의 가격(arr[0][0]) * 개수(arr[0][1])

if x == sum:
    print("Yes")
else:
    print("No")
