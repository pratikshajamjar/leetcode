class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        v = []
        
        for i in range(len(nums) - 1, -1, -1):
            k += nums[i]
            v.append(k % 10)
            k //= 10
        
        while k > 0:
            v.append(k % 10)
            k //= 10
        
        v.reverse()
        
        return v