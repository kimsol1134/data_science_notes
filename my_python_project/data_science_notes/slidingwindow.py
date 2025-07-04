N, M = map(int, input().split())
arr = [int(v) for v in input().split()]

start = 0
end = M-1
cur_sum = 0
for i in range(M):
    cur_sum += arr[i]
max_sum = cur_sum


while True:
    if cur_sum > max_sum :
        max_sum = cur_sum
        if end < N:
            cur_sum -= arr[start]
            start +=1
            end +=1
            if end == N :
                break
            cur_sum += arr[end]
    else :
        if end < N :
            cur_sum -= arr[start]
            start +=1
            end +=1
            if end == N :
                break
            cur_sum += arr[end]

print(max_sum)


### gpt 추천 버전

N, M = map(int, input().split())
arr = [int(v) for v in input().split()]

cur_sum = sum(arr[:M])
max_sum = cur_sum

for i in range(M,N):
    cur_sum += arr[i] # 오른쪽 끝 값 추가
    cur_sum -= arr[i-M] # 왼쪽 끝 값 제거
    if cur_sum > max_sum:
        max_sum = cur_sum
print(max_sum)