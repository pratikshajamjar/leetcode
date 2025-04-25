class Solution:
    def countInterestingSubarrays(self, a: List[int], m: int, k: int) -> int:
        c,p=0,Counter([0]);return sum((p[((c:=c+(x%m==k))-k)%m],p.update([c%m]))[0]for x in a)