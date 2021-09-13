from collections import deque

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
count = 0
arr_idx = 0
q = [x for x in range(1, 1 + n)]
q = deque(q)

ql = deque(q)
qr = deque(q)

while True:
    #print('ql: ' + str(ql))
    #print('qr: ' + str(qr))

    if arr_idx == len(arr):
        break

    if arr[arr_idx] == ql[0]:
        ql.popleft()
        qr = deque(ql)
        arr_idx += 1
    elif arr[arr_idx] == qr[0]:
        qr.popleft()
        ql = deque(qr)
        arr_idx += 1
    else:
        ql.append(ql.popleft())
        qr.appendleft(qr.pop())
        count += 1

print(count)