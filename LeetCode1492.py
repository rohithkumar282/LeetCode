'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/the-kth-factor-of-n/
'''


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor=[]
        for i in range(1,int(n/2)+1):
            if n%i==0:
                factor.append(i)
        factor.append(n)
        if len(factor)<k:
            return -1
        else:
            return factor[k-1]
