'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/number-of-1-bits/
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).lstrip('0b').count('1')
