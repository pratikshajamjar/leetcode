class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return ' '.join(s[a:b] for a, b in pairwise([0]+spaces+[len(s)]))     