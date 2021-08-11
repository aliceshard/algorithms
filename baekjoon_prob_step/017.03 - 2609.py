from sys import stdin, stdout

def sol():
    arr = list(map(int,input().split()))
    prime_table = [True for a in range(0, 10001)]
    prime_num = []
    prime_table[0] = False
    prime_table[1] = False
    for i in range(2, 10001):
        if prime_table[i] == True:
            prime_num.append(i)
            mul = 2
            while mul * i < 10001:
                prime_table[mul * i] = False
                mul += 1
    prime_num_exp_a = [0 for a in range(0, len(prime_num))]
    prime_num_exp_b = [0 for a in range(0, len(prime_num))]

    # 소인수 분해
    for i in range(0, len(prime_num)):
        while arr[0] % prime_num[i] == 0:
            prime_num_exp_a[i] += 1
            arr[0] /= prime_num[i]
        while arr[1] % prime_num[i] == 0:
            prime_num_exp_b[i] += 1
            arr[1] /= prime_num[i]

    # 정리
    min_multiple = 1
    max_factor = 1
    for i in range(0, len(prime_num)):
        if max(prime_num_exp_a[i], prime_num_exp_b[i]) != 0:
            min_multiple *= pow(prime_num[i], max(prime_num_exp_a[i], prime_num_exp_b[i]))
        if min(prime_num_exp_a[i], prime_num_exp_b[i]) != 0:
            max_factor *= pow(prime_num[i], min(prime_num_exp_a[i], prime_num_exp_b[i]))

    print(max_factor)
    print(min_multiple)

if __name__ == '__main__':
    sol()