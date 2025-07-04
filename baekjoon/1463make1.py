'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
'''

# 처음엔 무조건 3으로 나누어본다
# 안되면 2로 나누거나 1을 뺀다
# 다시 3으로 나누어 본다
# 반복 해서 1까지 된다음 적은 수 넣기

# n = int(input())
# cnt = 0
# while n != 1 :
#     if n == 2:
#         cnt = 1
#         break
#     if n % 3 == 0 :
#         n = n / 3
#         cnt +=1
#     elif (n-1) % 3 == 0 :
#         n = (n-1) /3
#         cnt +=2
#     elif (n-2) % 3 == 0 :
#         n = (n-2) % 3 
#         cnt += 3
#     elif n % 2 == 0:
#         n = n / 2
#         cnt +=1
#     else :
#         n = n-1
#         cnt +=1

# print(cnt)
#====위 방법은 시간초과 =====

#dp 
n = int(input())

dp = [float('inf')] * (n+1) # dp[i]는 i를 1로 만들기 위한 최소 계산 수
dp[1] = 0
if n >=2:
    dp[2]=1
if n >=3:
    dp[3] =1

for i in range(4, n+1):
    if i%3 == 0 and dp[i//3] != float('inf'):
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0 and dp[i//2] != float('inf'):
        dp[i] = min(dp[i], dp[i//2]+1)
    if dp[i-1] != float('inf'):
        dp[i] = min(dp[i], dp[i-1]+1)

print(dp[n])