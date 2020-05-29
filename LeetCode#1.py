'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/two-sum/
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if target==nums[i]+nums[j]:
                    return [i,j]
                    k=1
                    break
            if k==1:
                break
