'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/hamming-distance/
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = list(str(bin(x))[2:])
        x2 = list(str(bin(y))[2:])
        count = 0
        if len(x2) > len(x1):
            x1 = (len(x2) - len(x1)) * [0] + x1
        elif len(x1) > len(x2):
            x2 = (len(x1) - len(x2)) * [0] + x2
        for i,j in zip(x1,x2):
            if i == '1' or j =="1":
                if i != j:
                    count += 1
        return count
