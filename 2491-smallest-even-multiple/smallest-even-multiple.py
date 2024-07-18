class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        c = n
        while c % n or c % 2 :
            c += 1
        return c