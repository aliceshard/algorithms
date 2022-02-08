import sys

def swap(a, b):
    global heap
    temp = heap[a]
    heap[a] = heap[b]
    heap[b] = temp

def upHeapify(idx):
    global heap, size
    parent = idx // 2
    while parent >= 1:
        if heap[parent] < heap[idx]:
            return
        swap(parent, idx)
        idx = parent
        parent = parent // 2

def downHeapify(idx):
    global heap, size
    left = idx * 2
    while left <= size:
        right = left + 1
        if right <= size:
           if heap[left] > heap[right]:
               left = right
        if heap[left] > heap[idx]:
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
