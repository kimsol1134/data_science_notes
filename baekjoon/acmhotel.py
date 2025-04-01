T = int(input())
for _ in range(T):
    num=0
    H, W, N = map(int,input().split())
    room = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(1,W+1):
        for j in range(H,0,-1):
            num +=1
            if num == N:
                if i < 10:
                    ans = str(H+1-j)+str(0)+str(i)
                else : 
                    ans = str(H+1-j)+str(i)

    ans = int(ans)
    print(ans)