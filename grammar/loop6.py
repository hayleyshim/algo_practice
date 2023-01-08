def solution(N,M):

    answer = 0

    for i in range(N, M+1):
        if i %2 ==0:
            answer += i*i
    return answer

N = 4
M = 7
ret = solution(N,M)

print("solution 함수의 반환 값은", ret, "입니다")