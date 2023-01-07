def solution(data):
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt


data1 = [1,2,3,4,5,6,7,8,9,10]
ret1 = solution(data1)

print("Solution: return value of the function is", ret1, ".")

data2 = [1,1,1,1,1,1,1,1,1,9]
ret2 = solution(data2)

print("Solution: retrun value of the function is", ret2, ".")