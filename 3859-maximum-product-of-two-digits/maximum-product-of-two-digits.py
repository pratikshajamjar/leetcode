class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert the integer to a string to easily access each digit
        s = str(n)
        
        # Sort the digits in ascending order
        sorted_digits = sorted(s)
        
        # Extract the two largest digits (last two after sorting)
        return (int(sorted_digits[-1]) * int(sorted_digits[-2]))