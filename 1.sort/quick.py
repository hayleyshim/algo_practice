# 퀵정렬, O(logN) 빠른 알고리즘
# 하나의 숫자를 기준으로 양쪽 옆에 정렬
array = [40, 35, 27]

numbers = [40, 35, 27, 50, 75]

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number <= pivot]
        greater = [number for number in array[1:] if number > pivot]

        #less = array[1:]
        print('less:', less)
        print('greater', greater)
        return quick_sort(less) + [pivot] + quick_sort(greater)


result = quick_sort(numbers)
print(result)



