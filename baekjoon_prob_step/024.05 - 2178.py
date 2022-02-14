from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
count_graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = deque([[0,0]])
visited[0][0] = True
count_graph[0][0] = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while len(queue) != 0:
    y, x = queue.popleft()
    if x == m and y == n:
        break
    for i in range(4):
        nX = x + dx[i]
        nY = y + dy[i]

        if 0 <= nX < m and 0 <= nY < n:
            if graph[nY][nX] == 1 and not visited[nY][nX]:
                visited[nY][nX] = True
                queue.append([nY, nX])
                count_graph[nY][nX] += count_graph[y][x] + 1
print(count_graph[n - 1][m - 1])