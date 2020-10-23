'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
'''

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)-1):
            result.append(max(arr[i+1:]))
        result.append(-1)
        return result
