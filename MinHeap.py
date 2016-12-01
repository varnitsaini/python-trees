"""
Illustrating the Min Heap

Space Complexity : O(n)
Time Complexity : O(nlogn)

Where n is number of nodes
"""


def minHeapify(arr, i):

    left = 2 * i + 1
    right = 2 * i + 2
    arrLen = len(arr) - 1

    if left <= arrLen and arr[left] < arr[i]:
        smallest = left
    else:
        smallest = i

    if right <= arrLen and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        minHeapify(arr, smallest)



def buildMinHeap(arr):

    for i in range(len(arr)/2 + 1, -1, -1):
        minHeapify(arr, i)

arr = [5, 1, 9, 2, 6, 8, 0, 7]

buildMinHeap(arr)

print arr