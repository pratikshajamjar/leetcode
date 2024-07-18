class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi, ma = float('inf'), 0
        for i in nums:
            if i > ma:
                ma = i
            if i < mi:
                mi = i
        lcd = 1
        while True:
            if ma * lcd % mi == 0:
                lcd *= ma
                break
            lcd += 1
        return ma * mi // lcd