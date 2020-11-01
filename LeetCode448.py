'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nos = set(range(1,len(nums)+1))
        nums = set(nums)
        return list(all_nos-nums)
