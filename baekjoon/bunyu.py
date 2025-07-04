T = int(input()) #test number
num = 0
for _ in range(T):
    k = int(input()) #k층
    n = int(input()) #n호
    for i in range(1,k+1):
        for j in range(1,n+1):
            num += j



'''
재귀 인가?

2층 1 ,1+1+2 ,1+1+2+1+2+3, 1+1+2+1+2+3+1+2+3+4
1층  1 1+2 1+2+3 1+2+3+4
0층  1 2 3 4 5 6 7
'''
