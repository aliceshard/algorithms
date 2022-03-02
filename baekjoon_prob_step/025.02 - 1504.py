import sys
import heapq
input = sys.stdin.readline
INF = 0xffffff

## # of vertexes: n, # of edges: m, starting node: k
n, e = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c]) # b = dest_node, c = distance
    graph[b].append([a, c])
v1, v2 = map(int, input().split())
queue = []
distance = [INF] * (n+1)

def dijkstra(start):
    global queue
    heapq.heappush(queue, [start, 0]) # start_node, local_dist
    distance[start] = 0

    while len(queue) != 0:
        current_node, dist = heapq.heappop(queue)
        if distance[current_node] < dist:
            continue

        for i in graph[current_node]:
            dest_node = i[0]
            local_dist = i[1]

            cost = dist + local_dist
            if cost < distance[dest_node]:
                distance[dest_node] = cost
                heapq.heappush(queue, [dest_node, cost])

dijkstra(1)
cost_acc1 = distance[v1]
distance = [INF] * (n+1)
dijkstra(v1)
cost_acc1 += distance[v2]
distance = [INF] * (n+1)
dijkstra(v2)
cost_acc1 += distance[n]
distance = [INF] * (n+1)

dijkstra(1)
cost_acc2 = distance[v2]
distance = [INF] * (n+1)
dijkstra(v2)
cost_acc2 += distance[v1]
distance = [INF] * (n+1)
dijkstra(v1)
cost_acc2 += distance[n]
distance = [INF] * (n+1)

min_val = min(cost_acc1, cost_acc2)
if min_val >= INF:
    print('-1')
else:
    print(min_val)