def solution(a, b):
    answer = 0

    if a <= b :
        for i in range(a, b+1):
            answer += i

    elif a >= b:
        for i in range(b, a+1):
            answer += i
    elif a == b:
        answer = a

    return answer


def solution2(a, b):
    answer = 0

    if a > b:
        a, b = b, a

    for n in range(a, b+1):
        answer += n
    return answer

# sample 1
a = 3
b = 5
res = solution(a, b)
res2 = solution2(a, b)


print(res)
print(res2)


# sample 1
a = 3
b = 3
res = solution(a, b)
res2 = solution2(a, b)

print(res)
print(res2)


# sample 1
a = 5
b = 3
res = solution(a, b)
res2 = solution2(a, b)

print(res)
print(res2)
