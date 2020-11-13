'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
'''
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        result = 0
        for i in range(L,R+1):
            count = list(bin(i)[2:]).count('1')
            c = 0
            for j in range(1,(count//2)+1):
                if count%j==0:
                    c = c+1
            if c==1:
                result = result+1
        return result
