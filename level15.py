"""
#24416
피보나치 수 재귀호출 의사 코드
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}

fib(n){
    return 1 if(n=1 or n=2) else (f[n] = f[n-1]+f[n-2];
}
"""

def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

def fibonacci(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1, 1
    cnt2=0

    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt2

n = int(input())
print(f(n),fibonacci(n))

#9184
"""
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

"""
import sys
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
# 매번 값을 계산하도록 하는 형식이 아닌 한 번 계산된 값은 저장
# dp[] 3중 리스트를 만들어서 값을 저장할 수 있게 해준다.
# 범위는 20이 넘어가게 되면 다 20으로 만들기 때문에
# 인덱스 0~20 까지 쓸수 있도록 21로 잡는다.

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]


    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        break
    ans = w(a,b,c)
    print("w(%d, %d, %d) = %d" %(a, b, c, ans))
