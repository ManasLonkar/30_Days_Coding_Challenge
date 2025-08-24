from collections import defaultdict
from typing import List   # import this

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:   # fixed here
            key = "".join(sorted(word))
            anagram[key].append(word)

        return list(anagram.values())
