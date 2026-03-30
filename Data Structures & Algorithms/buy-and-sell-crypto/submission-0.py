class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        res = 0
        while R < len(prices):
            if prices[L] < prices[R]:
                diff = prices[R] - prices[L]
                res = max(res, diff)
            else:
                L = R
            R += 1
        return res
