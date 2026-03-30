class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for L in range(len(numbers)):
            R = len(numbers) - 1
            while L < R:
                if numbers[L] + numbers[R] == target:
                    return [L + 1, R + 1]
                R -=1