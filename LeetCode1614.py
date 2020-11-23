'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
'''
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_depth = 0
        for ele in s:
            if ele is "(":
                count += 1
            elif ele is ")":
                if max_depth < count:
                    max_depth = count
                count -= 1
        return max_depth
