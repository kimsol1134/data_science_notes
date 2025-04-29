import sys

#n 가로, m 세로, 질의 횟수 k
n , m , k = map(int, sys.stdin.readline().split())

# 원본 땅값 배열 및 누적합 배열 초기화
arr = [[0] * 1001 for _ in range(10001)]
p_Sum = [[0] * 1001 for _ in range(1001)]

#입력받은 땅값 배열을 arr에 저장하고 동시에 누적합 배열 pSum계산
for i in range(1, n+1) :
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(1, m+1):
        arr[i][j] = row[j-1]
        #누적합 공식 
        pSum[i][j] = (
            pSum[i-1][j] +
            pSum[i][j-1] - 
            pSum[i-1][j-1] +
            arr[i][j] 
        )

for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    result = (
        pSum[c][d] - 
        pSum[c][b-1] - 
        pSum[a-1][d] +
        pSum[a-1][b-1]
    )
    print(result)