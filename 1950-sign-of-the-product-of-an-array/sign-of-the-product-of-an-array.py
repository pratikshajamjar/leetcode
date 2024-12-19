class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]<0:
                count+=1

        if count%2==0 and 0 not in nums:
            return 1
        elif 0 in nums:
            return 0 
        return -1 