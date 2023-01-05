# 문자열 내림차순

def solution(s):
    answer = list(s)
    answer = sorted(s, key = lambda x:x, reverse = True)
    answer = "".join(answer)
    return answer


s = "Zbcdefg"
res = solution(s)
print(res)

s = "TsBuacykd"
res = solution(s)
print(res)

