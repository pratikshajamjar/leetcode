class Solution:
    def countSegments(self, s: str) -> int:
        count=0
        words=s.split()
        for word in words:
            count+=1
        return count

        