from sys import stdin, stdout

def sol():
    # init section
    n = int(input())
    input_arr = []
    for i in range(1, n+1):
        temp = map(int, input().split())
        temp_list = list(temp)
        input_arr.append(temp_list)
    input_arr.sort(key=lambda x: (x[1], x[0]))
    count = 1
    #print(input_arr)

    # greedy section
    current = input_arr[0]
    for i in range(1, n):
        if(current[1] <= input_arr[i][0]):
            current = input_arr[i]
            count += 1

    print(count)


if __name__ == '__main__':
    sol()