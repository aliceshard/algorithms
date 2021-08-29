from collections import deque

c = int(input())
for i in range(0, c):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr2 = [(i, arr[i]) for i in range(0,n)]
    max_pr = max(arr)
    q2 = deque(arr2)

    pr_cnt = 0
    while len(q2) != 0:
        if q2[0][1] < max_pr:
            q2.append(q2.popleft())
            continue

        pr_cnt += 1
        if q2[0][0] == m:
            print(pr_cnt)
            break
        q2.popleft()
        max_pr = max(list(q2), key=lambda x:x[1])[1]