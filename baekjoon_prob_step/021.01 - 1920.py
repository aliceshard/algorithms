import sys

def solve(target):
    global narr
    left_idx = 0
    right_idx = len(narr) - 1
    while True:
        if left_idx == right_idx and narr[left_idx] != target:
            return '0'

        mid_idx = (right_idx + left_idx) // 2
        if narr[mid_idx] == target:
            return '1'
        elif narr[mid_idx] < target:
            left_idx = mid_idx + 1
            continue
        elif narr[mid_idx] > target:
            right_idx = mid_idx - 1
            continue


n = int(sys.stdin.readline())
narr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
marr = list(map(int, sys.stdin.readline().split()))
narr.sort()

narr_max = max(narr)
narr_min = min(narr)

for i in marr:
    if i < narr_min or i > narr_max:
        print('0')
        continue
    elif i == narr_max or i == narr_min:
        print('1')
        continue

    ans = solve(i)
    print(ans)