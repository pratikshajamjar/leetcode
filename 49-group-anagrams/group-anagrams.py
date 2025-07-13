from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the word to use as a key
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
