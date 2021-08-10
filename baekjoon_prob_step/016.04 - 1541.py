from sys import stdin, stdout
import re

def sol():
    # init section
    s = input()
    num_arr = re.split('[+-]',s)
    opr_arr = re.split('[0-9]',s)
    opr_arr = [c for c in opr_arr if c]
    num_arr = list(map(int, num_arr))
    n = len(num_arr)
    #print(num_arr)
    #print(opr_arr)

    # greedy section
    tally = num_arr[0]
    temp = 0
    start_idx = 0
    while start_idx < n - 1 and opr_arr[start_idx] == '+':
        tally += num_arr[start_idx + 1]
        start_idx += 1

    for i in range(start_idx, n-1):
        if (opr_arr[i] == '-'):
            tally -= temp
            temp = num_arr[i + 1]
        elif (opr_arr[i] == '+'):
            temp += num_arr[i + 1]
    tally -= temp
    print(tally)

if __name__ == '__main__':
    sol()