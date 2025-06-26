from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # pointer for where the next valid element goes
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # overwrite nums in place
                k += 1
        return k
