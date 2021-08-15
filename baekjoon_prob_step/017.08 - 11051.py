from sys import stdin, stdout

def GCD(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b

def sol():
    n = int(input())
    arr = []
    for i in range(0,n):
        arr.append(int(input()))
    proc = []
    for i in range(0,n-1):
        proc.append(abs(arr[i] - arr[i+1]))

    # process
    gcd_num = 1000000001
    if len(proc) == 1:
        gcd_num = proc[0]
    else:
        for i in range(0,len(proc) - 1):
            gcd_num = min(gcd_num, GCD(proc[i], proc[i+1]))

    # get factors
    i = 2
    proc2 = []
    proc2.append(gcd_num)
    while i <= int(gcd_num**(1/2)) + 1:
        if gcd_num % i == 0:
            proc2.append(i)
            if(i != (gcd_num // i)):
                proc2.append(gcd_num // i)
        i += 1

    proc2.sort()
    proc2 = set(proc2)
    proc2 = list(proc2)
    for i in range(0, len(proc2)):
        print(proc2[i], end=' ')

if __name__ == '__main__':
    sol()