class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        l = len(nums)
        for i in range(0,l,2):
            s+=min(nums[i],nums[i+1])
        return s