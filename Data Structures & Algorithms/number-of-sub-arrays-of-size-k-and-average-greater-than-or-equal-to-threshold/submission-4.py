class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        j = 0
        for R in range(len(arr)):
            if R - L + 1 == k:
                avg_arr = arr[L: R+1]
                if sum(avg_arr) / k >= threshold:
                    j += 1
                L+=1
        return j
