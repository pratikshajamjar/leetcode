from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums).most_common(k)
        return [num for num,freq in x]