class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        max = 0
        min = prices[0]
        for i in range(len(prices)):
            sum = prices[i]-min
            if(sum>max):
                max = sum
            if(prices[i]<min):
                min = prices[i]
        return max