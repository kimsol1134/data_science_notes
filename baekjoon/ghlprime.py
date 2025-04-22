import math
M = int(input())
cnt = 0
for _ in range(M):
    N = int(input())
    ans = True
    if str(N) == str(N)[::-1]:
        if N <2 :
            ans = False
        else :
            for i in range(2, int(math.sqrt(N))+1):
                if N % i == 0 :
                    ans = False
                    break
        if ans == True :
            cnt +=1
print(cnt)
            
## 해답

def is_palindrome(s):
    return s == s[::-1]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0 :
            return False
    return True

n = int(input())
cnt = 0 
for _ in range(n):
    N = input()
    if is_palindrome(N) and is_prime(int(N)):
        cnt +=1
print(cnt)