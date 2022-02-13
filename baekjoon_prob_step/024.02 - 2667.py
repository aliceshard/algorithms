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
n = int(input())

graph = [[] for _ in range((n + 2) ** 2 + 1)] # 1-indexed
visited = [False] * ((n + 2) ** 2) # 1-indexed

arr = [['0'] for _ in range(n + 1)] # 1-indexed
arr[0] = ['0' for _ in range(n + 2)]
for i in range(1,n + 1):
    arr[i] = arr[i] + list(input()) + ['0']
arr.append(['0' for _ in range(n + 2)])

# Graph initialization
for i in range(1,n + 1):
    for j in range(1,n + 1):
        if arr[i][j] == '1' and arr[i+1][j] == '1':
            graph[i * (n) + j].append((i+1) * (n) + j)
            graph[(i+1) * (n) + j].append(i * (n) + j)
        if arr[i][j] == '1' and arr[i][j+1] == '1':
            graph[i * (n) + (j+1)].append(i * (n) + j)
            graph[i * (n) + j].append(i * (n) + (j+1))
        if arr[i][j] == '1' and arr[i+1][j] != '1' and arr[i-1][j] != '1'\
            and arr[i][j+1] != '1' and arr[i][j-1] != '1':
            count_list.append(1)

# bfs loop
for i in range((n+1) ** 2):
    bfs(i)

count_list.sort()
print(len(count_list))
for i in range(len(count_list)):
    print(count_list[i])