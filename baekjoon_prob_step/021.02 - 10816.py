import sys

def solve(target):
    global narr
    left_idx = 0
    right_idx = len(narr)
    lower_bound = upper_bound = -1

    # finding lower bound
    while right_idx > left_idx:
        mid_idx = (right_idx + left_idx) // 2
        if narr[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx
    lower_bound = left_idx

    # finding upper bound
    left_idx = lower_bound
    right_idx = len(narr)
    while right_idx > left_idx:
        mid_idx = (right_idx + left_idx) // 2
        if narr[mid_idx] > target:
            right_idx = mid_idx
        else:
            left_idx = mid_idx + 1
    upper_bound = right_idx

    return upper_bound - lower_bound

n = int(sys.stdin.readline())
narr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
marr = list(map(int, sys.stdin.readline().split()))
narr.sort()

for i in marr:
    ans = solve(i)
    print(ans, end=' ')