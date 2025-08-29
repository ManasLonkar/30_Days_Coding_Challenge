class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""

        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                if s[j] in temp :
                    break
                temp += s[j]
            if len(temp) > len(longest):
                longest = temp
        
        return len(longest)
