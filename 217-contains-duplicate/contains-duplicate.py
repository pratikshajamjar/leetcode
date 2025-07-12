from collections import Counter
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        # If any element appears more than once, return True
        for freq in count.values():
            if freq > 1:
                return True
        return False
