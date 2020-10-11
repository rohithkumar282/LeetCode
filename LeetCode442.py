'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''

import collections as cln
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return (key for key, freq in cln.Counter(nums).items() if freq == 2)
