'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/contains-duplicate/submissions/
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = list(set(nums))
        if len(dup)==len(nums):
            return False
        else:
            return True
