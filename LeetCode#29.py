'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/divide-two-integers/
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = (int)(dividend/divisor)
        if n>=-2**31 and n<=2**31-1:
            return n
        else:
            return (2**31-1)
