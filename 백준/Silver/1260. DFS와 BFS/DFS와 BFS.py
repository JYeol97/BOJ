from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in sorted(graph[node]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력
n, m, start = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 무방향 그래프

# DFS
visited_dfs = [False] * (n + 1)
dfs(graph, start, visited_dfs)
print()

# BFS
visited_bfs = [False] * (n + 1)
bfs(graph, start, visited_bfs)
