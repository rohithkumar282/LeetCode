'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while(i<len(nums)):
            print(i)
            if nums[i]==nums[i-1]:
                del nums[i-1]
                i = i-1
            i = i+1
