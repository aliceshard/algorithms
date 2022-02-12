import sys

t = int(sys.stdin.readline().rstrip())
for i in range(0, t):
    k = int(input())
    dp = []
    sum = [0]

    # arr initialize (0-indexed)
    arr = list(map(int, input().split()))

    # sum initialize (1-indexed)
    sum.append(arr[0])
    for j in range(2, len(arr) + 1):
        sum.append(sum[j-1] + arr[j-1])

    # DP process (1-indexed)
    dp = [[0] * (k+1) for _ in range(k + 1)]
    # 1) adjacent elements initialize
    for m in range(1, k):
        dp[m][m+1] = arr[m-1] + arr[m]
    # 2) Build DP table loop
    for m in range(3, k+1): # 몇 칸을 동시에 볼 것인가? (3인 경우는 ["2 3 4" 5], [2 "3 4 5"] 두 경우를 보게 된다]
        for n in range(1, k - m + 2): # 어디를 시작점으로 할 것인가? (1인 경우는 ["2" 3 4 5], 2인 경우는 [2 "3" 4 5])
            min_val = 50000000
            for l in range(1, m): # 칸막이 offset (1인 경우는 [2 | 3 4 5], 2인 경우는 [2 3 | 4 5])
                 min_val = min(min_val, dp[n][n + l - 1] + dp[n + l][n + m - 1] + sum[n+m-1] - sum[n-1])
            dp[n][n + m - 1] = min_val
    print(dp[1][k])