'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/sort-array-by-increasing-frequency/
'''
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        final_result = []
        result = Counter(nums)
        result =  sorted(result.items(),reverse = True)
        result =  sorted(result, key = lambda x:x[1])
        for ele in result:
            final_result.extend([ele[0]]*ele[1])
        return (final_result)
