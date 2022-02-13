import sys
from collections import deque

def bfs(n):
    global count
    visited[n] = True
    queue = deque([n])
    while len(queue) != 0:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1

count = 0
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(0,m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
bfs(1)
print(count)