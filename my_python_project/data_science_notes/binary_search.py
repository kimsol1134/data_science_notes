def binary_search(arr, target):
    left = 0 # 인덱스 시작
    right = len(arr) -1 # 인덱스 끝
    cnt = 0 # 탐색 횟수 카운트

    while left <= right : 
        cnt +=1 # 반복 할때마다 카운트 +1
        mid = (left + right) // 2 
        if arr[mid] == target :
            return mid
        elif arr[mid] < target :
            left = mid+1 # 우측 탐색

        elif arr[mid] > target :
            right = mid-1 # 좌측 탐색
    return -1 # 값 없으면 -1 

arr = [1,3,5,7,9,11,13]
target = 11

result = binary_search(arr,target)
print(result)