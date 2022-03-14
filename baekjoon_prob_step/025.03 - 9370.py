import sys
import heapq
input = sys.stdin.readline
INF = 20000000
graph = []

def dijkstra(start):
    global graph
    q = []
    heapq.heappush(q, [0, start]) # [dist, now]
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)
    distance[start] = 0

    while len(q) != 0:
        dist, now = heapq.heappop(q)

        if visited[now] is True:
            continue
        visited[now] = True

        for i in graph[now]:
            dest = i[0]
            local_dist = i[1]

            cost = dist + local_dist
            if cost <= distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, [cost, dest])
    return distance

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    smell_dist = 0
    graph = [[] for __ in range(n+1)]
    dest_cand = []

    for __ in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            smell_dist = d
        graph[a].append([b, d])
        graph[b].append([a, d])
    for __ in range(t):
        dest_cand.append(int(input()))

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    cand_q = []
    heapq.heapify(cand_q)
    for d in dest_cand:
        min_dist = dist_s[d]
        s_to_g = dist_s[g]
        s_to_h = dist_s[h]
        g_to_d = dist_g[d]
        h_to_d = dist_h[d]

        if min_dist == smell_dist + min(s_to_g + h_to_d, s_to_h + g_to_d):
            heapq.heappush(cand_q, d)

    while len(cand_q) != 0:
        print('{} '.format(heapq.heappop(cand_q)), end='')
    print()