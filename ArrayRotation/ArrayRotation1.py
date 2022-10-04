def solution(sample):
    answer = []

    return answer

def printList(sample):
    for ary in sample:
        for c in ary:
            print(c, end=" ")
        print()
    print()

data = [[3,7,1,9],
        [5,2,6,8],
        [6,4,7,1],
        [5,7,5,4]]

res = solution(data)
printList(res)

data = [[6,3,7,2,9],
        [8,5,4,6,7],
        [1,6,8,7,1],
        [4,5,7,9,4],
        [7,6,3,7,5]]

res = solution(data)
printList(res)

data = [[6,3,7,2,9,5,3,7],
        [3,6,8,8,5,3,6,7],
        [1,6,4,3,8,8,7,1],
        [6,4,5,7,5,2,9,4],
        [7,4,8,6,3,1,7,5],
        [5,6,3,9,8,2,7,1],
        [6,3,5,7,8,2,6,1],
        [2,4,4,9,6,1,2,5]]

res = solution(data)
printList(res)