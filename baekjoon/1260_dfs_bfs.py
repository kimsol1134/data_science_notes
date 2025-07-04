import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, v, visited, result):
    visited[v] = True # 현재 노드 방문 처리
    result.append(v) # 방문 순서 기록

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for neighbor in graph[v]:
        if not visited[neighbor]: # 아직 방문 안한 노드라면
            dfs(graph, neighbor, visited, result) # 재귀 호출로 깊이 들어감

def bfs(graph, start_node, visited, result):
    queue = deque([start_node]) # 시작 노드를 큐에 넣음
    visited[start_node] = True # 시작 노드 방문 처리

    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() # 큐에서 노드 하나 꺼냄
        result.append(v)

        # 꺼낸 노드와 연결된 아직 방문하지 않은 노드들을 큐에 삽입
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True # 방문 처리
                queue.append(neighbor)

# 1. 입력 처리 및 그래프 생성
n, m , v = map(int, input().split())
graph = [[] for _ in range(n+1)] # 1번부터 n번까지 사용하기 위해 n+1 크기로 생성

for _ in range(m):
    u, v = map(int, input().split())
    # 양방향 간선이므로 양쪽 모두에 추가
    graph[u].append(v)
    graph[v].append(u)

# 작은 번호 우선 방문 조건을 위해 각 정점의 인접 리스트 정렬
for i in range(1, n+1):
    graph[i].sort()

# 2. DFS
visited_dfs = [False] * (n+1)
dfs_result = [] # 방문 순서 저장 리스트
dfs(graph, v, visited_dfs, dfs_result)

# 3. BFS
visited_bfs = [False] * (n+1)
bfs_result = []
bfs(graph, v , visited_bfs, bfs_result)

# 4. 결과 출력
print(*dfs_result)
print(*bfs_result)