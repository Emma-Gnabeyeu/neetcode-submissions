class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfil = 0
        buyday,sellday = 0,1
        while sellday < len(prices):
            if prices[sellday] > prices[buyday]:
                MaxProfil=max(MaxProfil,prices[sellday]-prices[buyday])
            else:
                buyday=sellday
            sellday=sellday+1
        return MaxProfil
        