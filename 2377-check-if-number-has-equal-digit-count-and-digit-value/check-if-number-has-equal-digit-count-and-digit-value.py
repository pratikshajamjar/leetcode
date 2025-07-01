from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i, digit in enumerate(num):
            expected = int(digit)
            actual = count.get(str(i), 0)
            if expected != actual:
                return False
        return True
