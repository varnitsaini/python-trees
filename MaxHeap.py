"""
Illustrating the Max Heap

Space Complexity : O(n)
Time Complexity : O(nlogn)

Where n is number of nodes
"""


def maxHeapify(arr, i):

    left = 2 * i + 1
    right = 2 * i + 2
    arrLen = len(arr) - 1

    if left <= arrLen and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right <= arrLen and arr[right] > arr[largest]:
        largest = right

    if i != largest:
        arr[largest], arr[i] = arr[i], arr[largest]
        maxHeapify(arr, largest)


def buildMaxHeap(arr):

    for i in range(len(arr)/2, -1, -1):
        maxHeapify(arr, i)


arr = [5, 1, 9, 2, 6, 8, 0, 7]

buildMaxHeap(arr)

print arr