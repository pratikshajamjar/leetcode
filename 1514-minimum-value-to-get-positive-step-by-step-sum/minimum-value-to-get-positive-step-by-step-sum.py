class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        min_prefix_sum = 0

        for num in nums:
            total += num
            min_prefix_sum = min(min_prefix_sum, total)

        return 1 - min_prefix_sum
