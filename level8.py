"""
#10872
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

"""

def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))


#10870
"""
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
"""

def fibonachi(n):
    if n > 1:
        return fibonachi(n-1)+fibonachi(n-2)

    return n

n = int(input())
print(fibonachi(n))