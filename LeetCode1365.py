'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    count=count+1
            result.append(count)
        return result
