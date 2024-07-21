class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        steps=0
        while num1 and num2:
            if num1<num2:
                num2=num2-num1
            else:
                num1=num1-num2
            steps+=1
        return steps


        