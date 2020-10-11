'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/relative-sort-array/
'''

import collections as cln
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_result = []
        append = []
        dict_result = cln.Counter(arr1)
        for ele in arr2:
            arr2_result = arr2_result+[ele]*dict_result[ele]
        arr_temp = list(set(arr1))
        for ele in arr_temp:
            if ele not in arr2:
                append = append + [ele]*dict_result[ele]
        append.sort()
        arr2_result = arr2_result+append
        return arr2_result
