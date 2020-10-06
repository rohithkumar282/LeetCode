'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/consecutive-characters/
'''
class Solution:
    def maxPower(self, s: str) -> int:
        total = 0
        alphabets = list(set(s))
        for ele in alphabets:
            for i in range(1,len(s)+1):
                if ele*i in s:
                    if i>=total:
                        total=i
        return total
