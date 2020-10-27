'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
'''

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)-1):
            key=0
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    result.append(prices[i]-prices[j])
                    key=1
                    break
            if key==0:
                result.append(prices[i])
        result.append(prices[i+1])
        return result
