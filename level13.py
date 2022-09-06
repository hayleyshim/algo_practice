"""
#5086
첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

"""
while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')


#1037
"""
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성

첫째 줄에 N의 진짜 약수의 개수가 주어진다. 
둘째 줄에는 N의 진짜 약수가 주어진다.

"""

N = int(input())
M = list(map(int, input().split()))

N_max = max(M)
N_min = min(M)
print(N_max*N_min)