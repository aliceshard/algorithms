import sys
from collections import deque

def bfs(n):
    count = 0
    visited[n] = True
    queue = deque([n])
    while len(queue) != 0:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                if i == (m*n-1):
                    return count

n, m = list(map(int,input().split()))

# maze initialize
arr = [] # 1-indexed
arr.append(['0' for _ in range(0, m + 2)])
for i in range(0,n):
    arr.append(['0'] + list(input()) + ['0'])
arr.append(['0' for _ in range(0, m + 2)])

# tree initialize
graph = [[] for _ in range((n+1) * (m+1) + 1)] # 1-indexed
visited = [False] * ((n+1) * (m+1) + 1) # 1-indexed

for i in range(1,n+1):
    for j in range(1, m+1):
        if arr[i][j] == '1' and arr[i + 1][j] == '1':
            graph[i * m + j].append((i+1) * m + j)
            graph[(i+1) * m + j].append(i * m + j)
        if arr[i][j] == '1' and arr[i - 1][j] == '1':
            graph[i * m + j].append((i-1) * m + j)
            graph[(i-1) * m + j].append(i * m + j)
        if arr[i][j] == '1' and arr[i][j + 1] == '1':
            graph[i * m + j].append(i * m + (j+1))
            graph[i * m + (j+1)].append(i * m + j)
        if arr[i][j] == '1' and arr[i][j - 1] == '1':
            graph[i * m + j].append(i * m + (j-1))
            graph[i * m + (j-1)].append(i * m + j)
bfs(0)
print(count)