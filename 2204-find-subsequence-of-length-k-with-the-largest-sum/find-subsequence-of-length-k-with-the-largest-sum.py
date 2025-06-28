from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair elements with their original indices
        indexed = list(enumerate(nums))  # [(0, val0), (1, val1), ...]

        # Step 2: Sort based on value (descending) and keep top k
        top_k = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]

        # Step 3: Sort back based on index to maintain original order
        top_k_sorted = sorted(top_k, key=lambda x: x[0])

        # Step 4: Extract just the values
        result = [val for idx, val in top_k_sorted]
        return result
