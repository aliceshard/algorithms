m, n = list(map(int, input().split()))
MAX_VAL = 10001
arr = []
dp = []

# init table (1-indexed, framed with MAX_VAL)
arr.append([MAX_VAL for _ in range(0, n+2)])
for i in range(1, m+1):
    arr.append([MAX_VAL])
    temp_arr = list(map(int, input().split()))
    arr[i] = arr[i] + temp_arr
    arr[i].append(MAX_VAL)
arr.append([MAX_VAL for _ in range(0, n+2)])

# init dp (1-indexed)
dp = [[0] * (n+2) for _ in range(0, m+1)]
dp[m][n] = 1
dp.append([0] * (n+2))

for i in range(1, m + n - 1): # 가중치
    for j in range(0, i + 1): # x,y에 가중치를 조절
        y = m - j
        x = n - (i - j)
        if 0 < y <= m and 0 < x <= n:
            acc = 0
            if (arr[y][x] > arr[y+1][x] and dp[y+1][x] > 0):
                acc += dp[y+1][x]
            if (arr[y][x] > arr[y-1][x] and dp[y-1][x] > 0):
                acc += dp[y-1][x]
            if (arr[y][x] > arr[y][x+1] and dp[y][x+1] > 0):
                acc += dp[y][x+1]
            if (arr[y][x] > arr[y][x-1] and dp[y][x-1] > 0):
                acc += dp[y][x-1]
            dp[y][x] = acc
print(dp[1][1])
print()