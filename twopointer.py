N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
cur_sum = 0
cnt = 0

while True: #end와 start가 N 이 될때까지 반복
    if cur_sum >= M or end == N:
        if cur_sum == M :
            cnt +=1
        cur_sum -= arr[start]
        start +=1
    else :
        cur_sum += arr[end]
        end +=1
    
    if start ==N:
        break
print(count)