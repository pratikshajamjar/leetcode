class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = 0
       
        for i in range(1<<n):
            subset_xor = 0
            for j in range(n):
               
                if i & (1 << j):
                    subset_xor ^= nums[j]
            totalsum += subset_xor
        return totalsum