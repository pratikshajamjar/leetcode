class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        s=bin(n)[2:][::-1]
        if s.count('1')==1 and s.index('1')%2==0:
            return True
        return False
            