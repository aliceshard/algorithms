def dist_cal(point1, point2):
    x_dist = (point1[0] - point2[0]) ** 2
    y_dist = (point1[1] - point2[1]) ** 2
    return x_dist + y_dist

def solve(start, end):
    global inf, arr
    # print('start:{}, end:{}'.format(start, end))
    if start == end:
        # print('returned: {}'.format(inf))
        return inf
    mid_idx = (end + start) // 2
    min_dist = min(solve(start, mid_idx), solve(mid_idx + 1, end))

    # calculate candidates respect to x_pos
    arr2 = []
    left_idx = right_idx = mid_idx
    lborder_flag = rborder_flag = False

    arr2.append(arr[mid_idx])
    while right_idx != end:
        right_idx += 1
        if (arr[mid_idx][0] - arr[right_idx][0]) ** 2 < min_dist:
            arr2.append(arr[right_idx])
        else:
            break
    while left_idx != start:
        left_idx -= 1
        if (arr[mid_idx][0] - arr[left_idx][0]) ** 2 < min_dist:
            arr2.append(arr[left_idx])
        else:
            break

    # calculate candidates respect to y_pos
    arr2 = sorted(arr2, key=lambda x: x[1])
    #print(arr2)

    for i in range(0, len(arr2)):
        for j in range(i+1, len(arr2)):
            if arr2[i][0] == arr2[j][0] and arr2[i][1] == arr2[j][1]:
                return 0

            if (arr2[i][1] - arr2[j][1]) ** 2 < min_dist:
                min_dist = min(min_dist, dist_cal(arr2[i], arr2[j]))
            else:
                break

    # print('arr2: {}'.format(arr2))
    # print('returned: {}'.format(min_dist))
    return min_dist

def input_routine():
    global arr, inf
    n = int(input())
    # calculate respect to x_pos
    for i in range(0, n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    arr = sorted(arr, key=lambda x: x[0])
    ans = solve(0, len(arr) - 1)
    return ans

inf = 4000000001
arr = []
ans = input_routine()
print(ans)