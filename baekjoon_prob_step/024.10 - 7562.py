from collections import deque

dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())
for _ in range(t):
    l = int(input())
    start_pos = list(map(int, input().split()))
    dest_pos = list(map(int, input().split()))
    count_graph = [[0] * l for _ in range(l)]
    count_graph[start_pos[0]][start_pos[1]] = -1

    queue = deque([start_pos + [0]])
    while len(queue) != 0:
        v = queue.popleft()
        y = v[0]
        x = v[1]
        cur_count = v[2]

        if y == dest_pos[0] and x == dest_pos[1]:
            print(cur_count)
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < l and 0 <= ny < l:
                if count_graph[ny][nx] == 0:
                    count_graph[ny][nx] = cur_count + 1
                    queue.append([ny, nx, cur_count + 1])