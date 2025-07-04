# 반복문 이용한 피보나치 수열
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n) :
        a, b = b, a+b
    return a
    
print(fibonacci_iter(100))

# 메모이제이션 활용한 방법
memo = {}

def fib_memo(n):
    if n <= 1:
        return n
    if n in memo :
        result = memo[n]
    else :
        result = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = result
    return result

n = int(input())
print(fib_memo(n))


# 메모이제이션 + 재귀 이용한 탑다운 dp
def fibo_top_down(n, dp):
    if n <= 2 :
        return 1
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibo_top_down(n-1,dp) + fibo_top_down(n-2,dp)

    return dp[n]


n = int(input())
dp = [-1] * (n+1)

print(fibo_top_down(n, dp))

# 바텀업 bottom up 방식(반복문 + 테이블 채우기)

def fibo_bottom_up(n):
    dp = [0] * (n+1)

    # 초기 조건 (base case)
    dp[1]=dp[2]=1 

    # 점화식(dp[i] = dp[i-1] + dp[i-2]) 이용해 반복문으로 해결
    for i in range(3, n+1): 
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


