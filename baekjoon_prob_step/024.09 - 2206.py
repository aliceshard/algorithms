from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
queue = deque([[0, 0, 0]])

count_graph = [[[0] * m for _ in range(n)] for __ in range(2)]
count_graph[0][0][0] = 1
count_graph[1][0][0] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
min_val = 10000

while len(queue) != 0:
    y, x, breaked = queue.popleft()
    if x == m-1 and y == n-1:
        min_val = count_graph[breaked][y][x]
        break
    for i in range(4):
        nX = x + dx[i]
        nY = y + dy[i]
        if 0 <= nX < m and 0 <= nY < n:
            if graph[nY][nX] == 0 and count_graph[breaked][nY][nX] == 0:
                queue.append([nY, nX, breaked])
                count_graph[breaked][nY][nX] = count_graph[breaked][y][x] + 1
            if graph[nY][nX] == 1 and count_graph[breaked][nY][nX] == 0 and breaked == 0:
                queue.append([nY, nX, 1])
                count_graph[1][nY][nX] = count_graph[breaked][y][x] + 1


if n == m == 1:
    print(1)
elif min_val == 10000 or min_val == 0:
    print(-1)
else:
    print(min_val)