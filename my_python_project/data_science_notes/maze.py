import sys
from collections import deque

def escape_maze():
    input = sys.stdin.readline

    N, M = map(int, input().split()) # 미로 행(N)과 열(M)
    maze = [list(map(int, input().split())) for _ in range(N)] # N줄에 걸쳐 미로 정보 읽기
    dist = [[-1]* M for _ in range(N)] # 각 칸의 '최단 시간' 기록(-1 = 미방문)
    dist[0][0] = 0 # (1,1) 위치는 0초 (출발점) 

    dq = deque([(0,0)]) # BFS 큐 초기화-튜플(x,y) 삽입

    while dq: # 큐가 빌 때까지 반복
        x, y = dq.popleft() # 가장 먼저 들어온 좌표를 꺼냄

        if (x,y) == (N-1, M-1): # x,y가 도착점에 도착하면 답 출력 후 종료
            print(dist[x][y])
            return
        
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)): # 상하좌우 4방향 이동
            nx, ny = x + dx, y + dy
            # nx,ny가 미로 내에 있고
            if 0 <= nx < N and 0 <= ny <M and maze[nx][ny] == 1 and dist[nx][ny] == -1 : # 이동가능한 길이고 미방문한 곳이면
                dist[nx][ny] = dist[x][y] +1 # 방문하고 최단시간 업데이트
                dq.append((nx,ny)) # 다음에 탐색하도록 큐에 삽입
    
    print(-1) # 큐 다 돌고도 도착 못 하면 탈출 불가 

escape_maze()


def escape_maze():
    n, m = map(int, input().split()) # n,m 미로의 행과열
    maze = [list(map(int,input().split())) for _ in range(n)]
    dist = [[-1] * m for _ in range(n)] # 각 칸의 '최단 시간' 기록(-1 = 미방문)
    dist[0][0] = 0 #시작위치 0초로 초기화

    dq = deque([(0,0)]) # bfs큐 초기화- 튜플 (x,y) 삽입

    while dq: # 큐가 빌때까지 탐색
        x,y = dq.popleft() # 제일 먼저 들어온 좌표를 꺼냄

        if (x,y) == (n-1,m-1): # 도착점에 도착했다면
            print(dist[x][y])
            return
        
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)): # 상하좌우 4방향이동
            nx, ny = x + dx, y + dy
            # nx,ny가 미로내에 있고
            if 0<= nx < n and 0<= ny < m and maze[nx][ny] ==1 and dist[nx][ny] == -1 : # 이동가능한길 + 방문하지 않은곳이면
                dist[nx][ny] = dist[x][y] + 1 #방문하고 최단시간 업데이트
                dq.append((nx,ny))
    
    print(-1)
