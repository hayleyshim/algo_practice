# 이진 탐색, logN
# 중간값(mid index) 찾기


"""def binary_search(arr, target_num):
    mid_index = len(numbers) //2
    print("mid_index=>", mid_index)
    return -1"""

#print(binary_search(numbers, 4))

numbers = [1,2,3,5,6,7,8,9,10,11]


def binary_search(arr, target_num):
    start = 0
    end = len(arr) -1
    while(start <= end):
        mid_index = (start + end) // 2
        #print(start, end, mid_index)
        """index_value = arr[mid_index]
        print(start, end, mid_index, "index_value:", index_value)"""

        if arr[mid_index] == target_num:
            return mid_index
        elif arr[mid_index] < target_num:
            start = mid_index + 1
        elif arr[mid_index] > target_num:
            end = mid_index -1
        """print("start:", start, "end:", end, "mid_index:", mid_index,
              "target_num:", target_num, "index_value:", index_value)"""

    return -1

print(binary_search(numbers, 4))
