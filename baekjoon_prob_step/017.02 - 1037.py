n = int(input())
arr = list(map(int, input().split()))
arr= sorted(arr)

print(arr[0]*arr[n-1])