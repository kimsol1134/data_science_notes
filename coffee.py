n = int(input()) # 커피 1잔 가격

# 처음에 불가능한 값으로 초기화(큰 수)
dp = [float('inf')] * (n+1) # dp[i]: i원을 만들기 위한 최소 동전 개수
if n >= 3 :
    dp[3] = 1 
if n >= 5 :
    dp[5] = 1 #3원, 5원은 각각 동전 1개로 만들수있음

# 2원부터 100000원까지 각 금액을 만들 수 있는 최소 동전 개수 계산
for i in range(6, n+1): #3,5 제외하고 5보다 작으면 만들수 없음
    if dp[i-5] != float('inf'):
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if dp[i-3] != float('inf'):
        dp[i] = min(dp[i], dp[i - 5] + 1)
    print(f"dp[{i}] = {dp[i]}")

print(-1 if dp[n] == float('inf') else dp[n])
