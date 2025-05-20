import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) #재귀 깊이 늘리기

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)] #1번 인덱스에 1번 노드 0번 인덱스 안씀

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for neighbors in graph:
    neighbors.sort()

visited = [False] * (n+1) #1번 인덱스에 1번노드 방문여부 
visit_order = [0] *(n+1)

cnt = 0 
def dfs(start):
    global cnt
    visited[start] = True
    cnt +=1
    visit_order[start] = cnt

    for r in graph[start]:
        if not visited[r]:
            dfs(r)

dfs(r)

for i in range(1,n+1):
    print(visit_order[i])

