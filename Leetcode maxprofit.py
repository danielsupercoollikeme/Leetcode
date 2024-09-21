class Solution(object):
    def maxProfit_myself(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < n:
                n = prices[i]
            elif prices[i] - n > ans:
                ans = prices[i] - n
        return ans
    def solution_leftright(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        