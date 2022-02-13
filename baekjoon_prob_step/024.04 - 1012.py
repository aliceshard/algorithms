import sys
from collections import deque

def bfs(n):
    count = 1
    visited[n] = True
    queue = deque([n])
    while len(queue) != 0:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    if count != 1:
        count_list.append(count)

count_list = []
t = int(input())
for i in range(t):
    m, n, k = list(map(int,input().split()))
    graph = [[] for _ in range(m * n + 1)]  # 0-indexed
    visited = [False] * (m * n + 1)  # 0-indexed
    arr = [[0] * (m+1) for _ in range(n + 1)]  # 0-indexed, padded by 0 at right, bottom edge

    # Array initialization
    for j in range(k):
        x, y = list(map(int, input().split()))
        arr[y][x] = 1
    # Graph initialization
    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j] == 1 and arr[i+1][j] == 1:
                graph[i * m + j].append((i + 1) * m + j)
                graph[(i + 1) * m + j].append(i * m + j)
            if arr[i][j] == 1 and arr[i][j+1] == 1:
                graph[i * m + j].append(i * m + (j+1))
                graph[(i * m + (j+1))].append(i * m + j)
            if arr[i][j] == 1 and arr[i][j+1] != 1 and arr[i][j-1] != 1 and\
                arr[i+1][j] != 1 and arr[i-1][j] != 1:
                count_list.append(1)
    # bfs loop
    for j in range(n * m + 1):
        bfs(j)
    print(len(count_list))
    count_list = []