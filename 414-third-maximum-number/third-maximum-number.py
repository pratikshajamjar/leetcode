class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        if len(s)>2:
            s.remove(max(s))
            s.remove(max(s))
            return max(s)
        else:
            return max(s)