from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Apply the operations
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1  # Skip the next one since it is now 0
            i += 1

        # Step 2: Shift all zeros to the end
        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        while pos < n:
            nums[pos] = 0
            pos += 1

        return nums
