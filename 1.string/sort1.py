def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x : (x[n], x))
    return answer


# main
strings = ["sun", "bed", "car"]
n = 1

strings = ["abce", "abcd", "cdx"]
n = 2
print(res)