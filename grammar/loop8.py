def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += 1
        hp -= attack
        if hp <= 0:
            break
        hp += recovery
    return count

attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

print("solution 함수의 반환 값은", ret, "입니다")