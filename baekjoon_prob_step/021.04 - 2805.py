def cal_lan(target):
	global arr
	acc = 0
	for i in range(0, len(arr)):
		if target <= arr[i]:
			acc += (arr[i] - target)
		else:
			continue
	return acc

def solve(min_val, n):
    global arr
    left_val = 0
    right_val = max(arr) + 1
    max_len = -1

    while left_val < right_val:
        mid_val = (right_val + left_val) // 2
        cur_n = cal_lan(mid_val)
        #print('left: {}, right:{}, cur_n:{}'.format(left_val, right_val, cur_n)) 
        if cur_n < n:  
            right_val = mid_val
        elif cur_n >= n:
            max_len = max(max_len, mid_val)
            left_val = mid_val + 1
    return max_len

n, m = list(map(int,input().split()))
arr = list(map(int,input().split()))
min_val = min(arr)
print(solve(min_val, m))