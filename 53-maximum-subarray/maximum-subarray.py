class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Either start new or continue
            max_sum = max(max_sum, current_sum)        # Update global max
        return max_sum
