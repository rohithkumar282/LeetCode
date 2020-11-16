'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/check-array-formation-through-concatenation/
'''
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        result = []
        temp_dict = {}
        for ele in pieces:
            temp_dict[ele[0]] = ele

        for ele in arr:
            if ele in temp_dict:
                result.extend(temp_dict[ele])
        return arr == result
