import sys
from collections import deque

def escape_maze():
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    maze = [[int(v) for v in input().strip()] for _ in range(N)]
    dist = [[-1] * M for _ in range(N)]
    dist[0][0] = 1
    
    dq = deque([(0,0)])
    
    while dq:
        x, y = dq.popleft()
        
        if (x,y) == (N-1, M-1):
            print(dist[x][y])
            return
        
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx,ny))

escape_maze()



