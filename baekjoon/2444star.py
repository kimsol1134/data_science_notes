N = int(input())

for i in range(N):
    print(" "*(N-i)+"*"*(2*i-1))
for i in range(N,0,-1):
    if i == N:
        print("*"*(2*i-1))
    else :
        print(" "*(N-i)+"*"*(2*i-1))