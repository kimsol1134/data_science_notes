from collections import deque

#dfs
#인접리스트로 그래프 표현 
graph = [
    [], # 0번 노트 (미사용)
    [2, 3], # 1번 노드 -> 2,3
    [1], # 2번 노드 -> 1
    [1, 4, 5], # 3번 노드 -> 1, 4, 5
    [3], # 4번 노드 -> 3
    [3] # 5번 노드 -> 3
]

visited = [False] * 6 # 방문 여부 리스트 노드 1~5까지

def dfs(now):
    visited[now] = True # 현재 노드 방문 처리
    print(now, end=' ') # 현재 노드를 출력

    # 현재 노드와 연결된 인접 노드들 순회
    for next_node in graph[now]:
        if not visited[next_node]: #방문하지 않은 노드라면(False)
            dfs(next_node) # 재귀 호출로 깊이 우선 탐색


# bfs

graph = [
    [], # 0번 노트 (미사용)
    [2, 3], # 1번 노드 -> 2,3
    [1], # 2번 노드 -> 1
    [1, 4, 5], # 3번 노드 -> 1, 4, 5
    [3], # 4번 노드 -> 3
    [3] # 5번 노드 -> 3
]

visited = [False] * 6 # 방문 여부 리스트 노드 1~5까지

def bfs(start):
    queue = deque() # 큐 생성
    queue.append(start) # 시작 노드를 큐에 삽입
    visited[start] = True # 시작 노드를 방문 표시

    while queue:
        now = queue.popleft() # 큐에서 가장 앞 노드 꺼냄
        print(now, end = ' ') # 현재 노드 출력

        # 현재 노드와 연결된 모든 노드 확인
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True # 방문 표시
                queue.append(next_node)