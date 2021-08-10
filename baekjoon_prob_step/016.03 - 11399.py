from sys import stdin, stdout

def sol():
    # init section
    n = int(input())
    input_arr = list(map(int, input().split()))
    temp_arr = []
    input_arr.sort()
    tally = 0

    # greedy section
    for i in range(0, n):
        tally += input_arr[i]
        temp_arr.append(tally)
    result = sum(temp_arr)
    print(result)


if __name__ == '__main__':
    sol()