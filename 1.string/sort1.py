# sort, sorted 오름차순


def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x : (x[n],x))
    return answer

"""

test = [(1,8),(2,3),(7,9),(6,1),(4,5)]

# 기본 오름차순 정렬
print(sorted(test)) #[(1,8), (2,3), (4,5), (6,1), (7,9)]

# x를 기준으로 오름차순 정렬
print(sorted(test, key = lambda x:x)) #[(1,8),(2,3),(4,5),(6,1),(7,9)]

# x[0]을 기준으로 오름차순 정렬
print(sorted(test, key = lambda x:x[0])) #[(6,1),(2,3),(4,5),(1,8),(7,9)]

# x[1]을 기준으로 오름차순 정렬
print(sorted(test, key = lambda x:x[1])) #[(6,1),(2,3),(4,5),(1,8),(7,9)]

def solution(strings, n):
    answer = strings[:]

    for i in range(len(answer)):
        for j in range(len(answer)-1-i):
            if answer[j][n] > answer[j+1][n]:
                answer[j], answer[j+1] = answer[j+1], answer[j]
            elif answer[j][n] == answer[j+1][n]:
                if answer[j] > answer[j+1]:
                    answer[j], answer[j+1] = answer[j+1], answer[j]

    return answer
"""

# main
strings = ["sun", "bed", "car"]
n = 1

res = solution(strings, n)
print(res)

strings = ["abce", "abcd", "cdx"]
n = 2

res = solution(strings, n)
print(res)