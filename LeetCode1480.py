'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/running-sum-of-1d-array/
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final_result=[]
        sum1=0
        for i in range(len(nums)):
            sum1=sum1+nums[i]
            final_result.append(sum1)
        return final_result
