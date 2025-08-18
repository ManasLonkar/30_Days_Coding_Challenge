from typing import List

class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        arr = arr1[:m] + arr2[:n]
        arr.sort()
        mid = len(arr) // 2
        for i in range(mid):
            arr1[i] = arr[i]
        for i in range(mid,len(arr)):
            arr2[i - mid] = arr[i]

arr1 = [1,2,3,0,0,0]
m = 3
arr2 = [2,5,6]
n = 3
Solution().merge(arr1, m, arr2, n)  
print("arr1:", arr1[:m])  
print("arr2:", arr2[:n])