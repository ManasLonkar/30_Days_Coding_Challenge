from typing import List

def find_zero(arr):
    n = len(arr)
    result = []

    for start in range(n):
        total = 0
        for end in range(start,n):
            total += arr[end]
            if total == 0:
                result.append((start,end))
    return result