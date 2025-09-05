class Solution:
    def firstElement(self, arr, k): 
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        for i in arr:
            if count[i] == k:
                return i
                
        return -1