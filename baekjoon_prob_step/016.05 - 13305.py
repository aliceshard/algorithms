n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
tally = 0

i = 0
while i < n-1:
    cur_cost = cost[i]
    for j in range(i+1, n):
        if(cost[j] < cur_cost or j == n-1):
            total_dist = sum(dist[i:j])
            tally += total_dist * cur_cost
            i = j
            break

print(tally)