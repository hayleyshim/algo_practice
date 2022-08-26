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