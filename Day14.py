class Solution:
    def countSubstring(self, s, k):
        n = len(s)
        result = 0

        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(s[j])
                if len(distinct) == k:
                    result += 1
                elif len(distinct) > k:
                    break   
        return result