class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            countnum=0
            while num!=0:
                countnum+=1
                num=num//10
                
            if countnum%2==0:
                count+=1
        return count