#merge_sort() -> 배열을 계속 반으로 나누는 함수 -> 재귀호출, 분할
#merge()-> 나눈 배열을 정렬하며 다시 합치는 함수 -> 병합, 정렬하며 결합

def merge_sort(arr):
    # 베이스 케이스(종료조건) : 리스트에 원소가 하나만 있거나 없을때는 이미 정렬된 상태
    if len(arr)<=1:
        return arr
    
    # 1. 분할 : 리스트를 절반으로 나눔
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    # 2. 정복 : 각 부분을 재귀적으로 정렬
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # 3. 결합 : 정렬된 두 부분을 병합
    return merge(sorted_left, sorted_right)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    #두 리스트 모두 원소가 남아 있는 동안 반복
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx +=1
        else :
            merged.append(right[right_idx])
            right_idx +=1
    # 위 루프가 끝나면 하나의 리스트에는 원소가 남아있음
    # 남아있는 원소들을 결과 리스트 뒤에 그대로 이어 붙임
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

# 예시 사용
my_list = [5, 3, 8, 4, 9, 1, 6, 2, 7,7]
sorted_list = merge_sort(my_list)
print("원본 리스트:", my_list)
print("병합 정렬된 리스트:", sorted_list)