import sys

t = int(sys.stdin.readline().rstrip())
arr = []
dp = []

# arr initialize (0-indexed)
for j in range(0, t):
    arr.append(list(map(int, input().split())))

# DP process (1-indexed)
dp = [[0] * (t + 1) for _ in range(t + 1)]

# 1) adjacent elements initialize
for m in range(1, t):
    dp[m][m+1] = arr[m-1][0] * arr[m-1][1] * arr[m][1]

# 2) Build DP table loop
for m in range(3, t + 1): # 몇 칸을 동시에 볼 것인가? (3인 경우는 ["2 3 4" 5], [2 "3 4 5"] 두 경우를 보게 된다]
    for n in range(1, t - m + 2): # 어디를 시작점으로 할 것인가? (1인 경우는 ["2" 3 4 5], 2인 경우는 [2 "3" 4 5])
        min_val = 9876543210
        for l in range(1, m): # 칸막이 offset (1인 경우는 [2 | 3 4 5], 2인 경우는 [2 3 | 4 5])
            temp = min_val
            min_val = min(min_val, dp[n][n + l - 1] + dp[n + l][n + m - 1]
                          + (arr[n-1][0] * arr[n-1+l-1][1] * arr[n-1+m-1][1]))
        dp[n][n + m - 1] = min_val
print(dp[1][t])