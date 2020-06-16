'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro=float('-inf')
        for i in range(len(nums)):
            temp=nums[0:i]+nums[i+1:]
            temp=[(k-1)*(nums[i]-1) for k in temp]
            if max(temp)>=max_pro:
                max_pro=max(temp)
        return max_pro
