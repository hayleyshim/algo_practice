"""
#1712
노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용이 들며, 한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용이 든다고 한다.

예를 들어 A=1,000, B=70이라고 하자. 이 경우 노트북을 한 대 생산하는 데는 총 1,070만원이 들며, 열 대 생산하는 데는 총 1,700만원이 든다.

노트북 가격이 C만원으로 책정되었다고 한다. 일반적으로 생산 대수를 늘려 가다 보면 어느 순간 총 수입(판매비용)이 총 비용(=고정비용+가변비용)보다 많아지게 된다. 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(BREAK-EVEN POINT)이라고 한다.

A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
"""

A= 1000
B= 70

N = int(input())

C*N > A + B*N

a,b,c = map(int,input().split())

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)



"""
# 1978
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

"""

N = int(input())
data = list(map(int, input().split()))
prime_count = 0

for n in data:
   primeYes = True
   if n > 1:
       for i in range(2, n):
           if n % i == 0:
               primeYes = False
       if primeYes:
           prime_count += 1

print(prime_count)

#2292
"""
숫자 N이 주어졌을 때, 
벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 
몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성
예를 들면, 13까지는 3개, 58까지는 5개를 지난다.
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출
"""

n = int(input())
room = 1
cnt = 1

while n > room:
    room = room + (6*cnt)
    cnt += 1
print(cnt)

#2581
"""
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 
이들 소수의 합과 최솟값을 찾는 프로그램을 작성

M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 
둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
"""

start = int(input())
last = int(input())
sosu = []

for num in range(start, last+1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
        if error == 0 :
            sosu.append(num)

if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
