from collections import deque

n, k = list(map(int, input().split()))
visited = [False for _ in range(0,100001)]
queue = deque([[n]])

time = -1
escape_flag = False
while len(queue) != 0 and escape_flag is False:
    temp_queue = deque(queue.popleft())
    out_queue = deque([])
    while len(temp_queue) != 0:
        v = temp_queue.popleft()
        if v == k:
            escape_flag = True
            break
        if 0 <= v + 1 <= 100000 and visited[v+1] is False:
            visited[v+1] = True
            out_queue.append(v+1)
        if 0 <= v - 1 <= 100000 and visited[v-1] is False:
            visited[v-1] = True
            out_queue.append(v-1)
        if 0 <= v * 2 <= 100000 and visited[v*2] is False:
            visited[v*2] = True
            out_queue.append(v*2)
    queue.append(list(out_queue))
    time += 1
print(time)