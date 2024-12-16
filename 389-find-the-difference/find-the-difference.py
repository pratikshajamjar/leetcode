from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Count the frequency of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Find the character that has a higher count in t than in s
        for char in count_t:
            if count_t[char] > count_s[char]:
                return char
