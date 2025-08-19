class Solution:
    def leaders(self, arr):
        n = len(arr)
        leader = []
        max_from_right = float('-inf')
        for i in range(n-1,-1,-1):
            if arr[i] >= max_from_right:
                leader.append(arr[i])
                max_from_right = arr[i]
        
        leader.reverse()
        return leader