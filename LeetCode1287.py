'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0.25*len(arr)
        arr1 = list(set(arr))
        for ele in arr1:
            if arr.count(ele)>count:
                return ele
