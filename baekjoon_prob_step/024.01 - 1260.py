import sys
from collections import deque

# DFS
def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

# BFS
def bfs(n):
    visited[n] = True
    queue = deque([n])
    while len(queue) != 0:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().rstrip().split())
# graph, visited (1-indexed)
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)