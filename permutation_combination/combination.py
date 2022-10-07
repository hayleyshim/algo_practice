def combi1(nums, n, r, start):
    global visit1
    if r == 0:
        for i in range(len(nums)):
            if visit1[i]:
                print(nums[i], " ", end="")
            print()
            return
    for i in range(start, len(nums)):
        visit1[i] = True
        combi1(nums, n, r-1, i+1)
        visit1[i] = False


def combi2(nums, ans, n, r, idx, target):
    if r == 0:
        for i in ans:
            print(i, " ", end='')
        print()
        return

    if target == n:
        return

    ans[idx] = nums[target]
    combi2(nums, ans, n, r-1, idx+1, target+1)
    combi2(nums, ans, n, r, idx, target+1)


def recombination(nums, ans, n, r, idx, target):
    if r == 0:
        for i in ans:
            print(i, " ", end='')
        print()
        return

    if target == n:
        return

    ans[idx] = nums[target]
    recombination(nums, ans, n, r-1, idx+1, target)
    recombination(nums, ans, n, r, idx, target+1)

nums = [1, 2, 3, 4]
visit1 = [False for _ in range(len(nums))]
print("1. 조합(combination) - visit 리스트로 사용 여부 체크하는 방법")
combi1(nums, 4, 2, 0)
print()

r = 3
ans = [0 for _ in range(r)]
print("2. 조합(combination) - 재귀 호출로 사용 여부 결정하는 방법")
combi2(nums, ans, 4, r, 0, 0)
print()

r = 2
ans2 = [0 for _ in range(r)]
print("#3. 중복 조합")
recombination(nums, ans2, 4, r, 0, 0)