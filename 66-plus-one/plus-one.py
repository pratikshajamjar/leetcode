from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))  # convert list to string, then to int
        num += 1
        return [int(d) for d in str(num)]     # convert back to list of digits
