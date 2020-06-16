'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
'''

class Solution:
    def numberOfSteps (self, num: int) -> int:
        n = num
        count=0
        while(n!=0):
            if n%2==0:
                n=n/2
                count=count+1
            else:
                n=n-1
                count=count+1
        return count
