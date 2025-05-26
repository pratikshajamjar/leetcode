import heapq

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2, max3 = heapq.nlargest(3, nums)
        min1, min2 = heapq.nsmallest(2, nums)
        
        return max(max1 * max2 * max3, min1 * min2 * max1)