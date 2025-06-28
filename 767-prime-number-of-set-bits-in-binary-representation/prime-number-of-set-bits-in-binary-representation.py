class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            ones = bin(i).count('1')
            if self.is_prime(ones):
                count += 1
        return count
