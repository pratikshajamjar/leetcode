class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0 :
            return(False)
        if n==1 : 
            return(True)
        two_pow = 2 
        while two_pow<n :
            two_pow = two_pow * 2
        return(two_pow==n)