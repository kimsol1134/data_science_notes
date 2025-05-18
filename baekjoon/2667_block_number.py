from collections import deque

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 총 단지수 (컴포넌트 수)
#각 단지내 집수 오름차순으로 한줄씩 출력하기

# 상하좌우 움직임
move = [(1,0),(0,1),(-1,0),(0,-1)]
# bfs
def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    num_dan = 1

    while queue:
        x,y = queue.popleft()
        for dx, dy in move:
            nx,ny = x+dx,y+dy
            if 0<= nx <= n-1 and 0<= ny <= n-1:
                if graph[nx][ny] == 1 and visited[nx][ny] == False :
                    visited[nx][ny] = True
                    num_dan +=1
                    queue.append((nx,ny))
    # while 마지막 visited[x][y] 가 단지내 집 수
    return num_dan

cnt = 0
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] ==False:
            result.append(bfs(i,j))
            cnt +=1

result = sorted(result)
print(cnt)
for w in result:
    print(w)

