class Solution:
    def countDigits(self, num: int) -> int:
        org=num
        count=0
        while num!=0:
            last_digit=num%10
            if org%last_digit==0:
                count+=1
            num=num//10
        return count


        