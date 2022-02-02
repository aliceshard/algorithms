def cal_lan(target):
    global arr
    acc = 0
    for i in range(0, len(arr)):
        acc += (arr[i] // target)
    return acc

def solve(max_val, n):
    global arr
    left_val = 0
    right_val = max_val + 1
    max_len = -1

    while left_val < right_val:
        mid_val = (right_val + left_val) // 2
        cur_n = cal_lan(mid_val) # cur_n은 mid_val이 증가할수록 줄어들기만 한다.
        if cur_n < n: # (mid_val이 너무 길어서) 선이 부족하게 완성될 때 -> 선 길이를 더 줄여봐야함
            right_val = mid_val
        elif cur_n >= n: # (mid_val이 적당해서) 선이 목표치만큼 완성될 때 -> 선 길이를 더 늘려봐야함 (최대치까지)
            max_len = max(max_len, mid_val)
            left_val = mid_val + 1
    return max_len

k, n = list(map(int,input().split()))
arr = []
max_val = -1
for i in range(0, k):
    temp = int(input())
    max_val = max(max_val, temp)
    arr.append(temp)
print(solve(max_val, n))