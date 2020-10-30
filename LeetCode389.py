'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-the-difference/
'''

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        first_string = Counter(s)
        second_string = Counter(t)
        result = second_string - first_string
        return ''.join(result.keys())
