class Solution:
    def maxProduct(self, n: int) -> int:

       digit1, digit2 = nlargest(2, list(map(int, str(n))))

       return digit1 * digit2   