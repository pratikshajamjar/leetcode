class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # Since one number is missing, total range is 0 to n
        total_sum = (n * (n + 1)) // 2
        sum_of_array = sum(nums)
        return total_sum - sum_of_array
