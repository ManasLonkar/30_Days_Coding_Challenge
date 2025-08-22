class Solution:
    def reverseWords(self, s: str) -> str:
        a =s.split()
        reversed_a = a[::-1]
        return " ".join(reversed_a)
        