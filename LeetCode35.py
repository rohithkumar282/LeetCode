'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/search-insert-position/
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pos=0
        if target > nums[n-1]:
            pos = n
        else:
            for i in range(n):
                if nums[i]>=target:
                    pos=i
                    break
        return pos
