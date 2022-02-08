def bin_search(arr, target):
    left_idx = 0
    right_idx = len(arr)

    while left_idx < right_idx:
        mid = (left_idx + right_idx) // 2
        if arr[mid] > target:
            right_idx = mid
        elif arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left_idx = mid + 1
    return right_idx

n = int(input())
arr = list(map(int, input().split()))
memo = [arr[0]]

for i in range(n):
    if arr[i] > memo[-1]:
        memo.append(arr[i])
    else:
        idx = bin_search(memo, arr[i])
        memo[idx] = arr[i]

print(len(memo))