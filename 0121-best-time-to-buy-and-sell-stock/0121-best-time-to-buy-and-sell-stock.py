class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        er=0
        b=0
        s=1
        while s<len(prices):
            if prices[b]>prices[s]:
                b=s
            elif prices[s]-prices[b]>er:
                er=prices[s]-prices[b]
            s+=1 
        
        if er>0:          
            return er
        else:
            return 0