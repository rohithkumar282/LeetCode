'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if prices:
            ele = prices[0]
            for ele1 in prices[1:]:
                if ele1>ele:
                    profit += ele1 - ele
                ele = ele1
        return profit
