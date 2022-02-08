def solve(n, k):
    right_val = n ** 2 + 1
    left_val = 1
    max_len = -1

    while left_val < right_val:
        mid_val = (right_val + left_val) // 2
        #print('left_val:{}, right_val:{}, mid_val:{}'.format(left_val, right_val, mid_val))
        count = 0
        for i in range(1, n + 1):
            if i * n <= mid_val:
                count += n
            else:
                count += mid_val // i

        if count > k: # count가 너무 크다 = 목표 숫자를 줄이자
            right_val = mid_val
        elif count == k: # count가 같다 = 더 큰 값도 가능한가?
            right_val = mid_val
        elif count < k: # count가 너무 작다 = 목표 숫자를 늘리자
            left_val = mid_val + 1
    return left_val


n = int(input())
k = int(input())
print(solve(n, k))