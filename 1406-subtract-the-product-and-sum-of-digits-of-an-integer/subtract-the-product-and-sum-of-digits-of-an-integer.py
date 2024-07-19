class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum=0
        while n!=0:
            last=n%10
            prod*=last
            sum+=last
            n=n//10
        return prod-sum
