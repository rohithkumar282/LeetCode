'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/split-a-string-in-balanced-strings/
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        pattern_count = 0
        for i in s:
            if i == 'L':
                pattern_count += 1
            else:
                pattern_count -= 1
            if pattern_count == 0:
                count += 1
        return count
