class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # orig=0
        orig=x
        sumi=0
        while x!=0:
            last=x%10
            sumi+=last
            x=x//10
        if orig%sumi==0:
            return sumi
        return -1
        