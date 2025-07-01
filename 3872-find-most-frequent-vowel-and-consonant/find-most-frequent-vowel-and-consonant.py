from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        v = []
        c = []

        for char in s:
            if char in vowels:
                v.append(char)
            else:
                c.append(char)

        countv = max(Counter(v).values()) if v else 0
        countc = max(Counter(c).values()) if c else 0

        return countv + countc
