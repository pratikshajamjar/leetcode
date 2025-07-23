from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        n=len(nums)
        for char,coun in count.items():
            if coun>n//3:
                ans.append(char)
                
        return ans
        

        