'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/power-of-two/
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        k=0
        for i in range(n):
            if 2**i==n:
                k=1
                return 'true'
                break
            if 2**i>n:
                break
        if k==1:
            return 'false'
