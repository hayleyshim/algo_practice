def solution(characters):
    result = ""
    result += characters[0]

    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result += characters[i]

    return result

characters = "senteeeennccccceeee"
ret = solution(characters)

print("Solution: return value of the function is", ret, ".")
