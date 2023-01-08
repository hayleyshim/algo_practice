def solution(words):
    answer = ''

    for a in words:
        if len(a) >= 5:
            answer += a
    if len(answer) <1:
        answer = "empty"
    return answer

words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1)

print("solution 함수의 반환 값은", ret1,"입니다")


word2 = ["yes", "i", "am"]
ret2 = solution(word2)

print("solution 함수의 반환 값은", ret2, "입니다.")

