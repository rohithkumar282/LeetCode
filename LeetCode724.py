'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-pivot-index/
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot=-1
        for i in range(len(nums)):
            if sum(nums[0:i])==sum(nums[i+1:]):
                pivot=i
                break
        return pivot
