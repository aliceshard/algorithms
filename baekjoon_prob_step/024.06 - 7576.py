from collections import deque

m, n = list(map(int, input().split()))
box = [] # 0-indexed
start_pos = [] # position format: (y_pos, x_pos), 0-indexed
fruit = m * n
for i in range(n): # iterating about y-pos
    temp = list(map(int, input().split()))
    for j in range(m): # iterating about x-pos
        if temp[j] == 1:
            start_pos.append([i, j])
        elif temp[j] == -1:
            fruit -= 1
    box.append(temp)

count_graph = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = deque(start_pos)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# bfs initialize
max_val = 0
count = 0
for v in queue:
    count_graph[v[0]][v[1]] = 0
    visited[v[0]][v[1]] = True
    count += 1
while len(queue) != 0:
    v = queue.popleft()
    y = v[0]
    x = v[1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if box[ny][nx] == 0 and visited[ny][nx] is False:
                queue.append([ny, nx])
                count_graph[ny][nx] = count_graph[y][x] + 1
                max_val = max(max_val, count_graph[ny][nx])
                count += 1
                visited[ny][nx] = True
            elif box[ny][nx] == -1 and visited[ny][nx] is False:
                visited[ny][nx] = True
                continue
if count == fruit:
    print(max_val)
else:
    print(-1)