'''
4개를 z 모양으로 돌면서 값 기록함
0,0 -> 0,1 -> 1,0 -> 1,1
그중에 2번째 값 기록

1개 남을때 까지 반복
'''

n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

def sol(n, x, y): #x,y 시작점(0,0)
    if n == 1 :
        return matrix[x][y]
       
    half = n //2

    val_1 = sol(half, x,y)
    val_2 = sol(half, x, y+half)
    val_3 = sol(half, x+half, y)
    val_4 = sol(half, x+half, y+half)
    block_elements = [val_1,val_2,val_3,val_4]
    block_elements.sort()
    return block_elements[-2]

    # 이제 다음 4칸으로 이동
    # x,y가 n-1 보다 커지면 안됨
    # x 먼저 +2씩 하다가 x+2가 n-1 보다 크게되면 x다시 0으로 y 를 y+2 로
    # 반복해서 하나만 남을때 까지

print(sol(n, 0, 0))




