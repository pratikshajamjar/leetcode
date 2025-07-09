class Solution:
    @staticmethod
    def maxFreeTime(eventTime, k, startTime, endTime):
        count = len(startTime)
        prefixSum = [0] * (count + 1)
        maxFree = 0

        # Compute prefix sum of all busy times
        for i in range(count):
            prefixSum[i + 1] = prefixSum[i] + (endTime[i] - startTime[i])

        # Sliding window of size k to find max free time
        for i in range(k - 1, count):
            # Total occupied time in this window
            occupied = prefixSum[i + 1] - prefixSum[i - k + 1]

            # Window start and end
            windowEnd = eventTime if i == count - 1 else startTime[i + 1]
            windowStart = 0 if i == k - 1 else endTime[i - k]

            # Free time is total window duration minus occupied
            freeTime = windowEnd - windowStart - occupied

            maxFree = max(maxFree, freeTime)

        return maxFree
