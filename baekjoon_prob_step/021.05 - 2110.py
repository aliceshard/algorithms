def solve(c):
    global arr
    right_val = arr[-1] - arr[0] + 1
    left_val = 1
    mid_val = 0
    max_len = -1

    while left_val < right_val:
        mid_val = (right_val + left_val) // 2
        count = 1
        crit_idx = 0
        for i in range(1,len(arr)):
            if arr[i] - arr[crit_idx] < mid_val:
                continue
            else:
                count += 1
                crit_idx = i

        if count > c: # count가 너무 크다 = 집거리가 너무 짧다
            max_len = max(max_len, mid_val)
            left_val = mid_val + 1
        elif count == c: # count가 같다 = 더 큰 값도 가능한가?
            max_len = max(max_len, mid_val)
            left_val = mid_val + 1
        elif count < c: # count가 너무 작다 = 집거리가 너무 길다
            right_val = mid_val
    return max_len


n, c = list(map(int,input().split()))
arr = []
min_len = 1000000001
for i in range(0, n):
    temp = int(input())
    arr.append(temp)
arr.sort()
print(solve(c))