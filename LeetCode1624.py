'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/largest-substring-between-two-equal-characters/
'''

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_count = -1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[j]==s[i]:
                    dist = j - i -1
                    if dist>=max_count:
                        max_count = dist
        return max_count
