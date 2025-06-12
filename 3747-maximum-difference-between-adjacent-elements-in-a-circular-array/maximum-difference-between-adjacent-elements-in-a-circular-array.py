class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff=0
        for i in range(len(nums)):
            diff=abs(nums[i]-nums[i-1])
            max_diff=max(max_diff,diff)
        return (max_diff)
        