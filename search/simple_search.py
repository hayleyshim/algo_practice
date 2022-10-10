# 단순 탐색, n

arr = [1,2,3,5,6,7,8,9,10,11]

def simple_search(arr, target_num):
    for index in range(0, len(arr)):
        print(index)

print(simple_search(arr,8))



def simple_search(arr, target_num):
    for index in range(0, len(arr)):
        print(arr[index])

print(simple_search(arr,8))


def simple_search(arr, target_num):
    for index in range(0, len(arr)):
        if arr[index] == target_num:
            return index

    return -1

print(simple_search(arr, 8))
print(simple_search(arr, 4))