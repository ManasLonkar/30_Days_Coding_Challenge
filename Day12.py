class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        while len(s) > 0:
            l = len(s)
            s= s.replace("()","").replace("{}","").replace("[]","")
            if l == len(s):
                return False
        return True
