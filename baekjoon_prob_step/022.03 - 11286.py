import sys

def swap(a, b):
    global size, heap
    temp = heap[a]
    heap[a] = heap[b]
    heap[b] = temp

def upHeapify(idx):
    global size, heap
    parent = idx // 2
    while parent >= 1:
        if abs(heap[parent]) < abs(heap[idx]):
            return
        elif abs(heap[parent]) == abs(heap[idx]) and heap[parent] < heap[idx]:
            return
        swap(parent, idx)
        idx = parent
        parent = parent // 2

def downHeapify(idx):
    global size, heap
    left = idx * 2
    while left <= size:
        right = left + 1
        if right <= size:
            if abs(heap[left]) > abs(heap[right]):
                left = right
            elif abs(heap[left]) == abs(heap[right]) and heap[left] > heap[right]:
                left = right
        if abs(heap[left]) > abs(heap[idx]):
            return
        elif abs(heap[left]) == abs(heap[idx]) and heap[idx] < heap[left]:
            return
        swap(left, idx)
        idx = left
        left = left * 2

def pop():
    global size, heap
    root = heap[1]
    heap[1] = heap[size]
    size -= 1
    downHeapify(1)
    heap.pop()
    return root

def addNode(data):
    global size, heap
    heap.append(data)
    size += 1
    upHeapify(size)

size = 0
n = int(input())
heap = [0]
for i in range(0, n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if size == 0:
            print('0')
        else:
            print(pop())
    else:
        addNode(x)
