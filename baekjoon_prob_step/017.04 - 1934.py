from sys import stdin, stdout

def sol():
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(list(map(int, input().split())))

    for i in range(0, n):
        mod = 0
        a, b = arr[i][0], arr[i][1]
        while arr[i][0] % arr[i][1] != 0:
            mod = arr[i][0] % arr[i][1]
            arr[i][0] = arr[i][1]
            arr[i][1] = mod
        print(int(a*b/arr[i][1]))


if __name__ == '__main__':
    sol()