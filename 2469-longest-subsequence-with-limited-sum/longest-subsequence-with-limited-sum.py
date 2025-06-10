class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        res = []
        for query in queries:
            max_idx = bisect_right(prefixSum, query) - 1
            res.append(max_idx)
        return res

