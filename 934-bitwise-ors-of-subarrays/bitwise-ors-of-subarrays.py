class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for num in arr:
            next_cur = {num | prev for prev in cur} | {num}
            cur = next_cur
            res |= cur
        return len(res)
