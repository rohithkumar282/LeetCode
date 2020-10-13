'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/single-number/
'''
import collections as cln
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_1 = cln.Counter(nums)
        for key,value in dict_1.items():
            if value==1:
                return int(key)
