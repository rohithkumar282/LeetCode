'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
'''

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        key = 0
        for i in range(len(nums)+1):
            count = 0
            for ele in nums:
                if ele>=i:
                    count = count+1
            if count == i:
                key=1
                return i
        if key==0:
            return -1
