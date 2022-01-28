# parameters are index of input array
def solve(start, end):
    global input_arr
    left_idx = start
    mid_idx = (start + end) // 2
    right_idx = end
    #print('left_idx: {}, right_idx: {}'.format(left_idx, right_idx))
    if start == end:
        #print('returned: {}'.format(input_arr[start]))
        return input_arr[start]
    area = max(solve(start, mid_idx), solve(mid_idx + 1, end)) # to be determined

    #if left_idx == 0 and right_idx == len(input_arr)-1:
    #    print('this is root case')

    left_idx = right_idx = mid_idx
    minH = input_arr[mid_idx]
    lborder_flag = False
    rborder_flag = False

    # There's only one idx displacement per loop
    while lborder_flag == False or rborder_flag == False:
        if left_idx == start:
            lborder_flag = True
        if right_idx == end:
            rborder_flag = True

        # case 1 : if mid_idx is surrounded with higher heights -> proceed both idx's
        if lborder_flag == False:
            if input_arr[left_idx - 1] >= input_arr[left_idx]:
                left_idx -= 1
                area = max(area, minH * (right_idx - left_idx + 1))
                continue
        elif rborder_flag == False:
            if input_arr[right_idx + 1] >= input_arr[right_idx]:
                right_idx += 1
                area = max(area, minH * (right_idx - left_idx + 1))
                continue

        # case 2 : if mid_idx is surrounded with lower heights
        # -> compare left_idx and right_idx and proceed the higher idx
        if lborder_flag == True and rborder_flag == False:
            right_idx += 1
            minH = min(minH, input_arr[right_idx])
            area = max(area, (right_idx - left_idx + 1) * minH)
            continue
        elif lborder_flag == False and rborder_flag == True:
            left_idx -= 1
            minH = min(minH, input_arr[left_idx])
            area = max(area, (right_idx - left_idx + 1) * minH)
            continue
        elif lborder_flag == False and rborder_flag == False:
            if input_arr[left_idx - 1] <= input_arr[right_idx + 1]:
                right_idx += 1
                minH = min(minH, input_arr[right_idx])
                area = max(area, (right_idx - left_idx + 1) * minH)
                continue
            elif input_arr[left_idx - 1] >= input_arr[right_idx + 1]:
                left_idx -= 1
                minH = min(minH, input_arr[left_idx])
                area = max(area, (right_idx - left_idx + 1) * minH)
                continue
    #print('returned: {}'.format(area))
    return area

input_arr = []
while True:
    arr = list(map(int, input().split()))
    input_arr = arr[1:]
    if arr[0] == 0:
        break
    ans = solve(0, len(input_arr)-1)
    print(ans)