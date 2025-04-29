def quick_sort(arr):
    # 베이스 케이스(종료조건): 리스트에 원소가 없거나 하나만 있으면 이미 정렬된 상태
    if len(arr) <= 1:
        return arr
    
    # 1. pivot선택 (간단하게 첫번째 원소 선택)
    pivot = arr[0]
    # pivot제외 나머지 리스트
    tail = arr[1:]

    # 2. 분할 : pivot보다 작거나 같은 원소들과 큰 원소들로 분리
    left_side = [x for x in tail if x <=pivot]
    right_side = [x for x in tail if x > pivot]

    # 3. 재귀 및 결합
    # 왼쪽 재귀적으로 정렬 + 피봇 + 오른쪽 재귀적으로 정렬
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


#예시

my_list = [5, 3, 8, 4 , 9, 1, 6, 2, 7]
sorted_list = quick_sort(my_list)
print(sorted_list)