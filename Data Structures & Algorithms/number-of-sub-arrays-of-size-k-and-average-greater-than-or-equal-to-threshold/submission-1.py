from itertools import accumulate
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        data = 0
        presum = [0, *accumulate(arr)]

        for i in range(len(arr) - k + 1):
            window_sum = presum[i + k] - presum[i]
            if window_sum / k >= threshold:
                data += 1
        return data
