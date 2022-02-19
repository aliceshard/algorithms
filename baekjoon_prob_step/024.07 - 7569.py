from collections import deque

m, n, h = list(map(int, input().split()))
box = [] # 0-indexed
start_pos = [] # position format: (z_pos, y_pos, x_pos), 0-indexed
fruit = m * n * h
for k in range(h): # iterating about z-pos
    temp_2d = []
    for i in range(n): # iterating about y-pos
        temp = list(map(int, input().split()))
        for j in range(m): # iterating about x-pos
            if temp[j] == 1:
                start_pos.append([k, i, j])
            elif temp[j] == -1:
                fruit -= 1
        temp_2d.append(temp)
    box.append(temp_2d)

count_graph = [[[-1] * m for __ in range(n)] for _ in range(h)]
visited = [[[False] * m for __ in range(n)] for _ in range(h)]
queue = deque(start_pos)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# bfs initialize
max_val = 0
count = 0
for v in queue:
    count_graph[v[0]][v[1]][v[2]] = 0
    visited[v[0]][v[1]][v[2]] = True
    count += 1
while len(queue) != 0:
    v = queue.popleft()
    z = v[0]
    y = v[1]
    x = v[2]

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if box[nz][ny][nx] == 0 and visited[nz][ny][nx] is False:
                queue.append([nz, ny, nx])
                count_graph[nz][ny][nx] = count_graph[z][y][x] + 1
                max_val = max(max_val, count_graph[nz][ny][nx])
                count += 1
                visited[nz][ny][nx] = True
            elif box[nz][ny][nx] == -1 and visited[nz][ny][nx] is False:
                visited[nz][ny][nx] = True
                continue
if count == fruit:
    print(max_val)
else:
    print(-1)