from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            original_num = num
            while num > 0:
                last_digit = num % 10
                if last_digit == 0 or original_num % last_digit != 0:
                    return False
                num //= 10
            return True

        res = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                res.append(num)
                
        return res