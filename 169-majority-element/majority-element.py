from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        n=len(nums)
        for num,couns in count.items():
            if couns>n//2:
                return num

        