'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/valid-perfect-square/
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        j = 1
        while(j<=num):
            if j==num:
                return True
            i = i+1
            j = i*i
        return False
