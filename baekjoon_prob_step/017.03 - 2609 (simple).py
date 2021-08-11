from sys import stdin, stdout

def sol():
    a, b = list(map(int,input().split()))
    GCD, LCM = 0, 0
    for i in range(1, min(a,b)+1):
        if a % i ==0 and b % i == 0:
            GCD = i
    LCM = a * b / GCD
    print(int(GCD))
    print(int(LCM))

if __name__ == '__main__':
    sol()