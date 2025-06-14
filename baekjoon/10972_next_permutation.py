# from itertools import permutations

# n = int(input())
# answer = tuple([int(x) for x in input().split()])

# per_list = sorted(list(permutations(answer, n)))

# if per_list.index(answer) == len(per_list)-1:
#     print(-1)
# else :
#     print(*per_list[per_list.index(answer)+1])

# 메모리 초과

# 다음 순열 알고리즘
n = int(input())
data = list(map(int, input().split()))

# 1. 기준점(i) 찾기
# 뒤에서부터 탐색하며 data[i-1] < data[i]를 만족하는 첫 지점을 찾습니다.
i = n-1
while i > 0 and data[i-1] >= data[i]:
    i -=1

# 만약 i가 0이라면 현재 순열이 마지막 순열이라는 뜻
if i <= 0:
    print(-1)
else :
    # 2. 교환할 대상(j) 찾기
    # 다시 뒤에서부터 탐색하며, data[i-1] 보다 큰 첫번째 값을 찾습니다.
    j = n-1
    while data[j] <= data[i-1]:
        j -=1
    # 3. i-1 위치의 값과 j 위치의 값 교환
    data[i-1], data[j] = data[j], data[i-1]

    # 4. i 위치부터 끝까지의 원소들을 뒤집기(오름차순 정렬)
    # data[i:]를 슬라이싱하여 뒤집은후, 다시 원래 리스트에 대입
    p = n-1
    while i < p:
        data[i], data[p] = data[p], data[i]
        i+=1
        p-=1
    print(*data)
