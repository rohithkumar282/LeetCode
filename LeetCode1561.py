'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
'''
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        n = len(piles)//3
        i = n
        while(i<=3*n-1):
            ans+=piles[i]
            i = i+2
        return ans
