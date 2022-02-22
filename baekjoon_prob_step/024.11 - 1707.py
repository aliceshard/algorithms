from collections import deque

k = int(input())
for _ in range(k):
    # inputs
    v, e = map(int, input().split())
    graph = [[] for __ in range(v+1)] # 1-indexed
    bipart_graph = [0] * (v+1)
    visited = [False for __ in range(v+1)] # 1-indexed
    queue = []
    for __ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    # bipartite graph detection
    fail_flag = False
    inspect_idx = 1
    while inspect_idx != v+1:
        if fail_flag is True:
            break

        if visited[inspect_idx] is True:
            inspect_idx += 1
        else:
            queue = deque([[inspect_idx, 1]])

        while len(queue) != 0:
            elm = queue.popleft()
            cur_vrtx = elm[0]
            cur_flag = elm[1]
            visited[cur_vrtx] = True

            for i in graph[cur_vrtx]:
                if visited[i] is False:
                    if cur_flag == 1:
                        queue.append([i, 2])
                        bipart_graph[i] = 2
                    elif cur_flag == 2:
                        queue.append([i, 1])
                        bipart_graph[i] = 1
                if visited[i] is True and cur_flag == bipart_graph[i]:
                    print('NO')
                    queue = deque([])
                    fail_flag = True
                    break

    if fail_flag is False:
        print('YES')