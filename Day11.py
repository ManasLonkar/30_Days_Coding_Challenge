from itertools import permutations
class Solution:
    def findPermutation(self, s):
        # Code here
        p = set("".join(i) for i in permutations(s))
        return list(p)