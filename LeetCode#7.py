'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/reverse-integer/
'''

class Solution:
    def reverse(self, x: int) -> int:
        sum1=0
        if x>=0 and x<=2**31-1:
            k=0
        elif x>=-2**31:
            k=1
            x=x*-1
        else:
            k=-1
            return 0
        while(x!=0):
            sum1=sum1*10+x%10
            x=(int)(x/10)
        if k==1 and -sum1>=-2**31:
            return -sum1
        elif k==0 and sum1>=0 and sum1<=2**31-1 :
            return sum1
        else:
            return 0
