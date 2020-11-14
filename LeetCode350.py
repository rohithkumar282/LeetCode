'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        for key in count1.keys():
            if key in count2.keys():
                result.extend([key]*min(count1[key],count2[key]))
        return result
