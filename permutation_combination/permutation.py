def permu1(nums, ans, n, r):
    global visit1
    if len(ans) == r:
        for i in ans:
            print(i, " ", end="")
        print()
        return

    for i in range(n):
        if visit1[i] == False:
            visit1[i] = True
            ans.append(nums[i])
            permu1(nums, ans, n, r)
            visit1[i] = False
            ans.pop()


def swap(nums, a, b):
    tmp = nums[a]
    nums[a] = nums[b]
    nums[b] = tmp
    

def permu2(nums, n, r, depth):
    if depth == r:
        for i in range(r):
            print(nums[i], " ", end='')

        print()
        return

    for i in range(depth, n):
        swap(nums, depth, i)
        permu2(nums, n, r, depth+1)
        swap(nums, depth, i)


def repermutation(nums, ans, n, r):
    if len(ans) == r:
        for i in ans:
            print(i, " ", end='')
        print()
        return

    for i in range(n):
        ans.append(nums[i])
        repermutation(nums, ans, n, r)
        ans.pop()

nums = [1,2,3,4]
ans = []
visit1 = [False for _ in range(len(nums))]
print("# 1. 순열(Permutation - visit 리스트로 사용 여부 체크하는 방법")
permu1(nums, ans, 4, 3)
print()

print("# 2. 순열(Permutation - 재귀 호출로 사용 여부 결정하는 방법 ")
permu2(nums, 4, 2, 0)
print()

ans2 = []
print("# 3. 중복 순열")
repermutation(nums, ans2, 4, 2)

