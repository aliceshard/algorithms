from sys import stdin, stdout

def sol():
    # init section
    n, k = map(int, (input().split()))
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    arr.append(0) # 1-indexed array
    arr = arr[::-1]

    # greedy section
    count = 0
    sum = 0
    for i in range(1, n+1):
        while sum + arr[i] <= k:
            sum += arr[i]
            count += 1
    print(count)

if __name__ == '__main__':
    sol()