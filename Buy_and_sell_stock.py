class Solution:
    def maxProfit(self, prices):
        mini=prices[0]
        profit=0
        for i in range(1,len(prices)):
            diff=prices[i]-mini
            profit=max(profit,diff)
            mini=min(mini,prices[i])
        return profit
 # 7 6 4 3 1
        # diff=0
        # profit=4
        # mini=3
p=[7,1,5,3,6,4]
t=Solution()
print(t.maxProfit(p))